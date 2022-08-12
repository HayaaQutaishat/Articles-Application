import json
from wsgiref.util import request_uri
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from final.models import Profile, User, Article, Categories, Comment, Rating
from django.contrib import messages
from django import forms
# Create your views here.

def index(request):
    return render(request, "final/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "final/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "final/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "final/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "final/register.html", {
                "message": "Email address already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "final/register.html")

def categories(request):
    categories = Categories.objects.all()
    return render(request, "final/categories.html", {
        "categories": categories
    })

def category(request, category_id):
    category = Categories.objects.get(pk=category_id)
    articles = Article.objects.filter(category=category).order_by('-date')
    return render(request, "final/category.html", {
        "articles": articles
    })

def article(request, article_id):
    article = Article.objects.get(pk=article_id)
    article_category = article.category
    comments = article.comments.all().order_by('-time')
    total_comments = article.comments.count()
    user = request.user
    in_read_later = False
    if user.is_authenticated:
        if article in user.read_later.all():
            in_read_later = True

    return render(request, "final/article.html", {
        "article": article,
        "comments": comments,
        "total_comments": total_comments,
        "article_category": article_category,
        "in_read_later": in_read_later
    })

@login_required
def comment(request, article_id):
        if request.method == "POST":
            comment = request.POST["comment"]
            article = Article.objects.get(pk=article_id)
            comment = Comment.objects.create(user=request.user,article=article,comment=comment)
            comment.save()
            messages.success(request, 'Comment successfully Added.')
            return HttpResponseRedirect(reverse("article", args=(article_id,)))
        return render(request, "final/article.html")

@login_required
def new_article(request):
    if request.method == "POST":
        category = Categories.objects.get(pk=int(request.POST["category"]))
        title = request.POST["title"]
        brief = request.POST["brief"]
        text = request.POST["text"]
        article = Article.objects.create(author=request.user,title=title, brief=brief, text=text, category=category)
        article.save()
        messages.success(request, 'Article successfully created.')
        return HttpResponseRedirect(reverse('category', kwargs={'category_id': category.id}))
    categories = Categories.objects.all()
    return render(request, "final/create_article.html", {
        "options": categories
    })

def search(request):
    if request.method == "POST":
        search = request.POST["search"]
        articles = Article.objects.filter(title__contains=search)
        return render(request, "final/search.html", {
            "articles": articles,
            "search": search
        })
    return render(request, "final/search.html")
    
def author(request, user):
    user = User.objects.get(username=user)
    user_profile = Profile.objects.get(user=user)
    user_articles = user.articles.all()
    return render(request, "final/author.html", {
        "user_articles": user_articles,
        "user_profile": user_profile,
        "user": user
    }) 

def random(request):
    random_article = Article.objects.order_by('?')[0]
    return render(request, "final/random.html", {
        "random_article": random_article
    })

def rating(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    # Check the data
    data = json.loads(request.body)
    id = data.get("id", "")
    article = Article.objects.get(pk=id)
    user = request.user
    score = data.get("score", "")
    rating = Rating.create(user=user, article=article, score=score)
    rating.save()
    return JsonResponse({"scroe": score }, status=201)


@login_required
def read_later(request):
    user = request.user
    user_articles = user.read_later.all()
    return render(request, "final/read_later.html", {
        "user_articles": user_articles
    })


@login_required
def read_later_add(request, article_id):
        if request.method == "POST":
            article = Article.objects.get(pk=article_id)
            user = request.user
            user.read_later.add(article)
            messages.success(request, 'Article successfully added to your Read Later.')
            return HttpResponseRedirect(reverse("read_later"))
        return render(request, "final/read_later.html")

@login_required
def read_later_remove(request, article_id):
        if request.method == "POST":
            article = Article.objects.get(pk=article_id)
            user = request.user
            user.read_later.remove(article)
            messages.success(request, 'Article successfully removed from your Read Later.')
            return HttpResponseRedirect(reverse("read_later"))
        return render(request, "final/read_later.html")


@login_required
def commentt(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    # Check the data
    data = json.loads(request.body)
    comment_id = data.get("comment_id", "")
    comment = Comment.objects.get(pk=comment_id)
    return JsonResponse(comment.comment, safe=False)


@login_required
def edit_comment(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)
    # Check the data
    data = json.loads(request.body)
    new_comment_text = data.get("new_comment", "")
    comment_id = data.get("comment_id", "")
    comment = Comment.objects.get(pk=comment_id)
    comment.comment = new_comment_text
    comment.save()
    return JsonResponse({"data": data}, status=201)


@login_required
def delete_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    article_category = article.category
    category_id = article_category.id
    article.delete()
    messages.success(request, 'Article successfully deleted.')
    return HttpResponseRedirect(reverse("category", args=(category_id,)))


