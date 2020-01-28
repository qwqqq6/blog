from django.contrib import admin
from .models import Label, Article, ExampleModel


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')


@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    pass