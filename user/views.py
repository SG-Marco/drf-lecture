from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework import permissions, status
from user.serializers import UserSerializer
from user.permissions import RegistedMoreThan5MINUser

'''
class UserView(APIView): # CBV 방식
    permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def get(self, request):
        return Response({'message': 'get method!!'})
        
    def post(self, request):
        return Response({'message': 'post method!!'})

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})
'''

class UserApiView(APIView):
    permission_classes = [RegistedMoreThan5MINUser] # 누구나 view 조회 가능
    # 유저 정보
    def get(self, request):
        # user = request.user
        # serializer에 queryset을 인자로 줄 경우 many=True 옵션을 사용해야 한다.
        # serialized_user_data = UserSerializer(request.user).data
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)

    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, **request.data)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})

        login(request, user)
        return Response({"message": "로그인 성공!!"})

    # 로그아웃
    def delete(self, request):

        logout(request)
        return Response({"message": "로그아웃 되었습니다"})

