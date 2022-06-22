from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework import permissions, status
from product.models import Product
from user.serializers import UserProfileSerializer, UserSerializer, UserSignupSerializer
from product.serializers import ProductSerializer
from Django.permissions import RegistedMoreThan5MINUser, IsJoinedMoreThan3DaysOrNoAuthenticatedReadOnly
import datetime
from django.db.models.query_utils import Q


class ProductView(APIView):
    permission_classes = [IsJoinedMoreThan3DaysOrNoAuthenticatedReadOnly]
    # permission_classes = [RegistedMoreThan5MINUser] # 누구나 view 조회 가능
    # 상품 조회
    def get(self, request):
        today = datetime.datetime.now().date()
        products = Product.objects.filter(post_start_day__lte = today, post_end_day__gte = today).order_by("-created_at")
        
        query = Q(user=request.user) | Q(post_start_day__lte = today, post_end_day__gte = today, is_active=True)
        products = Product.objects.filter(query)
        
        return Response(ProductSerializer(products, many=True).data, status=status.HTTP_200_OK)

    # 상품 등록
    def post(self, request):
        request.data["user"] = request.user.id
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 상품 정보 수정
    def put(self, request, obj_id):
        product = Product.objects.get(id=obj_id)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 상품 삭제
    def delete(self, request, obj_id):
        Product.objects.get(id=obj_id).delete()

        return Response({"message": "delete method!!"})


