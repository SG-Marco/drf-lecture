from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Article, Category, Comment


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
        # title / category / contents를 입력받아서 게시글을 작성하는 기능을 구현해주세요
        # - 만약 title이 5자 이하라면 게시글을 작성할 수 없다고 리턴해주세요
        #  - 만약 contents가 20자 이하라면 게시글을 작성할 수 없다고 리턴해주세요
        #  - 만약 카테고리가 지정되지 않았다면 카테고리를 지정해야 한다고 리턴해주세요
        title = request.data.get('title', '')
        if len(title) <= 5:
            return Response({'message': '제목은 6글자 이상이어야 합니다.'})
        content = request.data.get('content', '')
        if len(content) <= 20:
            return Response({'message': '글 내용은 21글자 이상이어야 합니다.'})
        try:    
            category = Category.objects.get(name=request.data.get('category', ''))
        except:
            return Response({'message': '글의 카테고리를 지정해야 합니다.'})

        Article(title=title, content=content, category=category).save()
        return Response({'message': '작성한 글이 저장되었습니다.'})

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})
