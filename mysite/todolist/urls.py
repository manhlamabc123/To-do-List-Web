from django.urls import path
from . import views

urlpatterns = [
    path('todolist_<str:list_name>/', views.todolist, name="todolist"),
    path('create_new_todolist/', views.create_new_todolist),
]