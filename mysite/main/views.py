from django.shortcuts import render
from todolist.models import ToDoLists

# Create your views here.
def home(response):
    user_first_todolist = ToDoLists.UserFirstList(response.user.id)
    return render(response, "main/home.html", {"user_first_todolist": user_first_todolist})