from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone
from rest_framework.exceptions import APIException
from rest_framework import status

SAFE_METHODS = ('GET', )

class RegistedMoreThan5MINUser(BasePermission):
    """
    가입 기준 5분 이상 지난 사용자만 접근 가능
    """
    message = '가입 후 5분 이상 지난 사용자만 사용하실 수 있습니다.'
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.join_date < (timezone.now() - timedelta(minutes=5)))


class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

class IsAdminOrIsJoinedWeekAgoOrIsAuthenticatedReadOnly(BasePermission):
    """
    admin 사용자는 모두 가능, 로그인 사용자는 조회만 가능
    """
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response ={
                    "detail": "서비스를 이용하기 위해 로그인 해주세요.",
                }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if user.is_authenticated and user.is_admin:
            return True
            
        elif user.is_authenticated and request.method in self.SAFE_METHODS:
            return True

        elif user.is_authenticated and request.user.join_date < (timezone.now() - timedelta(days=7)):
            return True
        
        return False
    

class IsJoinedMoreThan3DaysOrNoAuthenticatedReadOnly(BasePermission):
    """
    가입후 3일 이상된 회원은 상품등록 가능, 로그인 안하면 조회만 가능
    """
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user

        if user.is_authenticated and user.is_admin:
            return True

        elif not user.is_authenticated and request.method in self.SAFE_METHODS:
            return True
            
        elif user.is_authenticated and request.user.join_date < (timezone.now() - timedelta(days=3)):
            return True
        
        return False
