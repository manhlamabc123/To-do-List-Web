from django.urls import path
from . import views

urlpatterns = [
    path('todolist_<str:list_name>/', views.todolist, name="todolist"),
    path('create_new_todolist_<str:list_name>/', views.create_new_todolist),
    path('delete_todolist_<str:list_name>/', views.delete_todolist),
    path('deleted_todolist/', views.deleted_todolist),
    path('clicked_todolist_name_<str:list_name>/', views.clicked_todolist_name),
    path('edit_todolist_name_<str:list_name>/', views.edit_todolist_name),
    path('check_todolist_name/', views.check_todolist_name),
    path('update_check_box_<str:list_name>_<int:item_id>/', views.update_check_box),
    path('check_item_name/', views.check_item_name),
    path('check_item_description_update/', views.check_item_description_update),
    path('check_item_name_update/', views.check_item_name_update),
    path('update_new_item_<str:list_name>/', views.update_new_item),
    path('delete_item_<str:list_name>_<int:item_id>/', views.delete_item),
    path('clicked_item_name_<str:list_name>_<int:item_id>/', views.clicked_item_name),
    path('clicked_item_description_<str:list_name>_<int:item_id>/', views.clicked_item_description),
    path('update_item_name_<str:list_name>_<int:item_id>/', views.update_item_name),
    path('update_item_description_<str:list_name>_<int:item_id>/', views.update_item_description),
]