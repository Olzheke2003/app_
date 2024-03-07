from django.contrib import admin

from .models import Category, Comment, Rating, Request, RequestStatus, User

admin.site.register(Request)
admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(RequestStatus)
admin.site.register(Category)
admin.site.register(User)
