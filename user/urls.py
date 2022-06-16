from django.urls import path, include
from user import views

urlpatterns = [
    path('', views.UserApiView.as_view()),
]
