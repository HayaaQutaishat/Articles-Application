from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("category/<int:category_id>", views.category, name="category"),
    path("article/<int:article_id>", views.article, name="article"),
    path("comment/<int:article_id>", views.comment, name="comment"),
    # path("author/<str:user>", views.author, name="author"),
    path("new_article", views.new_article, name="new_article"),
    path("search", views.search, name="search"),
]