from django.shortcuts import render
from todolist.models import ToDoLists

# Create your views here.
def home(response):
    if response.user.is_authenticated:
        user_first_todolist = ToDoLists.UserFirstList(response.user.id)
    else:
        user_first_todolist = None
    return render(response, "main/home.html", {"user_first_todolist": user_first_todolist})