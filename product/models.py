from django.db import models

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    thumbnail = models.FileField("썸네일", upload_to="product/")
    description = models.TextField("본문", null=True)
    created_at = models.DateTimeField("글 작성 시간", auto_now_add=True)
    post_start_day = models.DateField("노출 시작일", null=True)
    post_end_day = models.DateField("노출 종료일", null=True)

    def __str__(self):
        return f"{self.user.username} 님이 작성하신 글입니다."

