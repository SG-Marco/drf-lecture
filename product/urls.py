from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    # user/
    path('', views.ProductView.as_view()),
    path('<int:obj_id>/', views.ProductView.as_view()),
]