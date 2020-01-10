from django.db import models


class Article(models.Model):  # 文章
    title = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    # label = models.ForeignKey

    def __str__(self):
        return str(self.title)


class Label(models.Model):  # 标签
    name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)