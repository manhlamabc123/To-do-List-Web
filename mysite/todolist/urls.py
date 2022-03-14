from django.urls import path
from . import views

urlpatterns = [
    path('todolist_<str:list_name>/', views.todolist, name="todolist"),
    path('create_new_todolist_<str:list_name>/', views.create_new_todolist),
    path('delete_todolist_<str:list_name>/', views.delete_todolist),
    path('deleted_todolist/', views.deleted_todolist),
]