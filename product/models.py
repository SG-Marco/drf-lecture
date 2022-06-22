from django.db import models

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=50)
    thumbnail = models.FileField("썸네일", upload_to="product/")
    description = models.TextField("본문", null=True)
    price = models.IntegerField("가격", default=0)
    created_at = models.DateTimeField("글 작성 시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정 시간", auto_now=True, null=True)
    post_start_day = models.DateField("노출 시작일", null=True)
    post_end_day = models.DateField("노출 종료일", null=True)
    is_active = models.BooleanField("활성화 여부", default=True)

    def __str__(self):
        return f"{self.user.username} 님이 작성하신 {self.title}글입니다."



class Review(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    product = models.ForeignKey('Product', verbose_name="상품", on_delete=models.CASCADE)
    contents = models.TextField("내용", null=True)
    rating = models.DecimalField("평점", max_digits=2, decimal_places=1)
    created_at = models.DateTimeField("글 작성 시간", auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} 님이 작성하신 {self.product.title} 리뷰입니다."
