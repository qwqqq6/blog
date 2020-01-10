from django.contrib import admin
from .models import Label, Article


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

