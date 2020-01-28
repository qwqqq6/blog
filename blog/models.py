from django.db import models
from mdeditor.fields import MDTextField


class Label(models.Model):  # 标签
    name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)


class ExampleModel(models.Model):
    name = models.CharField(max_length=10)
    content = MDTextField()


class Article(models.Model):  # 文章
    title = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    label = models.ManyToManyField(Label)
    # label = models.ForeignKey

    def __str__(self):
        return str(self.title)


