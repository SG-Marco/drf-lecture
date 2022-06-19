from rest_framework import serializers
from .models import Article, Comment, Category


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name"]



class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    category = CategorySerializer(many=True)
    class Meta:
        model = Article
        fields = ["title", "comment_set", "category"]





