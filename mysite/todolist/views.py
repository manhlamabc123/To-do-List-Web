from django.shortcuts import redirect, render
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

def create_new_todolist(response):
    user_todolist = list(ToDoLists.objects.filter(user_id = response.user.id).order_by('id'))
    new_todolist_name = f"List {user_todolist[-1].id + 1}"
    new_todolist = ToDoLists(user_id = response.user.id, name = new_todolist_name)
    new_todolist.save()
    return redirect(f"/todolist_{new_todolist_name}")