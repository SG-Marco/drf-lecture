from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ["title"]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["article.title", "comment"]




