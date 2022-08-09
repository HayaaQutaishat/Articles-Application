from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass

class Categories(models.Model):
    type = models.CharField(max_length=50)
    image = models.URLField(max_length=10000, blank=True, null=True)
    
    def __str__(self):
        return f"{self.type}"

class Article(models.Model):
    title = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    brief = models.TextField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True, related_name="categories")

    @classmethod
    def create(cls, author, title, brief, text, category):
        article = cls(author=author, title=title, brief=brief, text=text, category=category)
        return article

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    comment = models.CharField(max_length=5000)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, user, article, comment):
        comment = cls(user=user, article=article, comment=comment)
        return comment

    def __str__(self):
        return f"{self.comment}"


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=5000)
    

    def __str__(self):
        return f"{self.user}"