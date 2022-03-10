from multiprocessing import context
from django.shortcuts import render
from todolist.models import ToDoLists

# Create your views here.
def todolist(response, list_name):
    user_todolist = ToDoLists.objects.filter(user_id = response.user.id)
    now_todolist = ToDoLists.objects.get(name = list_name)
    context = {
        "user_todolist": user_todolist,
        "now_todolist": now_todolist
    }
    return render(response, "todolist/todolist.html", context)