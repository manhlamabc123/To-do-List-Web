from django.urls import path
from . import views

urlpatterns = [
    path('habit', views.habit),
]