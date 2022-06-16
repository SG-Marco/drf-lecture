from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Article


# Create your views here.
class ArticleView(APIView): # CBV 방식
    permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def get(self, request):
        articles = Article.objects.filter(author=request.user)
        article_titles = []
        for article in articles:
            article_titles.append(article.title)
        return Response({'message': article_titles})
        
    def post(self, request):
        return Response({'message': 'post method!!'})

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})
