from django.contrib import admin

from .models import Category, Question, Choice, UserSelection

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(UserSelection)
