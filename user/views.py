from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework import permissions, status
from user.serializers import UserProfileSerializer, UserSerializer, UserSignupSerializer
from Django.permissions import RegistedMoreThan5MINUser


class UserView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [RegistedMoreThan5MINUser] # 누구나 view 조회 가능
    # 사용자 정보 조회
    def get(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)

    # 회원가입
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 완료!!"})
        else:
            print(serializer.errors)
            return Response({"message": "가입 실패!!"})

    # 회원 정보 수정
    def put(self, request):
        return Response({"message": "put method!!"})

    # 회원 탈퇴
    def delete(self, request):
        return Response({"message": "delete method!!"})


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

