from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField("이름", max_length=50)
    description = models.TextField("설명")

    def __str__(self):
        return self.name
    
class Article(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    category = models.ManyToManyField(Category, verbose_name="카테고리")
    contents = models.TextField("본문", null=True)
    created_at = models.DateTimeField("글 작성 시간", auto_now_add=True)
    post_start_day = models.DateField("노출 시작일")
    post_end_day = models.DateField("노출 종료일")

    def __str__(self):
        return f"{self.user.username} 님이 작성하신 글입니다."


class Comment(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    article = models.ForeignKey('Article', verbose_name="게시글", on_delete=models.CASCADE)
    contents = models.TextField("본문", null=True)

    def __str__(self):
        return f"{self.article.title} / {self.contents}"

