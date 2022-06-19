from rest_framework.permissions import BasePermission
from datetime import timedelta
from django.utils import timezone

class RegistedMoreThan5MINUser(BasePermission):
    """
    가입 기준 5분 이상 지난 사용자만 접근 가능
    """
    message = '가입 후 5분 이상 지난 사용자만 사용하실 수 있습니다.'
    
    def has_permission(self, request, view):
        return bool(request.user and request.user.join_date < (timezone.now() - timedelta(minutes=5)))