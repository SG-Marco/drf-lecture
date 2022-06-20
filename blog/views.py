from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from blog.models import Article as ArticleModel
from Django.permissions import RegistedMoreThan5MINUser, IsAdminOrIsJoinedWeekAgoOrIsAuthenticatedReadOnly
import datetime

class ArticleView(APIView):
    # 로그인 한 사용자의 게시글 목록 return
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [RegistedMoreThan5MINUser]
    permission_classes = [IsAdminOrIsJoinedWeekAgoOrIsAuthenticatedReadOnly]

    def get(self, request):
        user = request.user
        # articles = ArticleModel.objects.filter(user=user)
        articles = ArticleModel.objects.filter(post_start_day__lte = datetime.datetime.now().date(), post_end_day__gte = datetime.datetime.now().date()).order_by("-created_at")

        titles = [article.title for article in articles] # list 축약 문법

        titles = []

        for article in articles:
            titles.append(article.title)

        return Response({"article_list": titles})
    
    def post(self, request):
        user = request.user
        title = request.data.get("title", "")
        contents = request.data.get("contents", "")
        category = request.data.get("category", [])

        if len(title) <= 5:
            return Response({"error": "타이틀은 5자 이상 작정해야 합니다."}, status=status.HTTP_400_BAD_REQUEST)

        if len(contents) <= 20:
            return Response({"error": "내용은 20자 이상 작정해야 합니다."}, status=status.HTTP_400_BAD_REQUEST)

        if not category:
            return Response({"error": "카테고리가 지정되지 않았습니다."}, status=status.HTTP_400_BAD_REQUEST)

        article = ArticleModel(
            user=user,
            title=title,
            contents=contents
        )
        article.save()
        article.category.add(*category)
        return Response({"message": "게시글 작성 완료!!"}, status=status.HTTP_200_OK)





