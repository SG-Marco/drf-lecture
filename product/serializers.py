from rest_framework import serializers

from blog.models import Category as CategoryModel
from blog.models import Article as ArticleModel
from blog.models import Comment as CommentModel

from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

from product.models import Product as ProductModel
from product.models import Review as ReviewModel

from user.serializers import UserSerializer

from blog.serializers import ArticleSerializer, CommentSerializer
from django.utils import timezone
import math


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


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReviewModel
        fields = ["user","product","contents","rating","created_at",]
        

class ProductSerializer(serializers.ModelSerializer):

    average_rating = serializers.SerializerMethodField()
    latest_review = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        reviews = ReviewModel.objects.filter(product=obj)
        rating_sum = 0
        for review in reviews:
            rating_sum += review.rating
        try:    
            average_rating = round(rating_sum * 10 / len(reviews)) /10
        except:
            average_rating = None
        return average_rating
    
    def get_latest_review(self, obj):
        latest_review = ReviewSerializer(ReviewModel.objects.filter(product=obj).order_by("-created_at").first()).data
        return latest_review

    class Meta:
        model = ProductModel
        fields = ["user", "title", "description", "price", "thumbnail", "created_at", "updated_at", "post_start_day", "post_end_day", "is_active", "average_rating", "latest_review"]

 # validate ?????? ?????? ??? serializer?????? ???????????? ?????? ????????? validation??? ??????
    def validate(self, data):
        # custom validation pattern
        today = timezone.now().date()
        if data.get("post_end_day", 9999-12-31) < today:
            # validation??? ???????????? ?????? ?????? ValidationError class ??????
            raise serializers.ValidationError(
                    # custom validation error message
                    detail={"error": "?????? ?????? ????????? ???????????? ?????? ?????????."},
                )

        # validation??? ????????? ?????? ?????? data return
        return data

    def create(self, *args, **kwargs):
        product = super().create(*args, **kwargs)
        sentence = product.description
        created_at = product.created_at
        sentence = sentence + f"{created_at.date()}??? ????????? ???????????????."
        product.description = sentence
        product.save()
        return product

    def update(self, obj, *args, **kwargs):
        sentence = obj.description
        updated_at = obj.updated_at
        sentence = f"{updated_at.date()}??? ?????????????????????." + sentence
        obj.description = sentence
        obj.save()
        return obj
