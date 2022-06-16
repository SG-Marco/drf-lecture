import pstats
from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):

    name = models.CharField("카테고리 이름", max_length=30, default="")
    description = models.TextField("설명")

    class Meta:
        pass

    def __str__(self):
        return self.name


class Article(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=30)
    category = models.ManyToManyField("Category", verbose_name="Category")
    content = models.TextField()

    class Meta:
        pass

    def __str__(self):
        return f'{self.author.username}/{self.title}'


