from rest_framework import serializers

from blog.models import Category as CategoryModel
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

from product.models import Product as ProductModel


from blog.serializers import ArticleSerializer, CommentSerializer


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user

    def update(self, *args, **kwargs):
        user = super().create(*args, **kwargs)
        p = user.password
        user.set_password(p)
        user.save()
        return user




class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = ["user", "title", "description", "thumbnail", "created_at", "post_start_day", "post_end_day"]



