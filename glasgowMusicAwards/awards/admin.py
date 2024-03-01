from django.contrib import admin
from awards.models import UserProfile, Post, Comment, Genre, Artist, Vote, Content

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Vote)
admin.site.register(Content)

    