from django.contrib import admin
from final.models import User, Article, Categories, Comment, Profile

# Register your models here.
admin.site.register(Article)
admin.site.register(Categories)
admin.site.register(Comment)
admin.site.register(Profile)


