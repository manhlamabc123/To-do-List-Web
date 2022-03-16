from http.client import HTTPResponse
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from todolist.models import ToDoLists, Items
import re

# Create your views here.
def todolist(response, list_name):
    user_todolist = ToDoLists.objects.filter(user_id = response.user.id)
    now_todolist = ToDoLists.objects.get(name = list_name)
    context = {
        "user_todolist": user_todolist,
        "now_todolist": now_todolist
    }
    return render(response, "todolist/todolist.html", context)

def create_new_todolist(response, list_name):
    new_todolist_name = ToDoLists.ListNameGenerator(response)
    if new_todolist_name != None:
        ToDoLists.CreateNewToDoList(response, new_todolist_name)
        return redirect(f"/todolist_{new_todolist_name}")
    else:
        return redirect(f"/todolist_{list_name}")

def delete_todolist(response, list_name):
    new_list = ToDoLists.DeleteTodolist(response, response.user.id, list_name)
    if new_list != None:
        return redirect(f"/todolist_{new_list}")
    return redirect("/deleted_todolist")

def deleted_todolist(response):
    user_todolist = ToDoLists.objects.filter(user_id = response.user.id)
    context = {
        "user_todolist": user_todolist,
    }
    return render(response, "todolist/deleted_todolist.html", context)

def clicked_todolist_name(response, list_name):
    now_todolist = ToDoLists.objects.get(name = list_name, user_id = response.user.id)
    return render(response, "todolist/replace_todolist_name.html", {"now_todolist": now_todolist})

def edit_todolist_name(response, list_name):
    if response.method == "POST":
        new_name = response.POST.get("new_name")
        change_list = ToDoLists.objects.get(name = list_name, user_id = response.user.id)
        change_list.name = new_name
        change_list.save()
    return redirect(f"/todolist_{new_name}/")

def check_for_special_character(string): 
    special_character = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    return any(ext in string for ext in special_character)

def check_todolist_name(response):
    if response.method == "POST":
        new_name = response.POST.get("new_name")
        todolist = list(ToDoLists.objects.filter(name = new_name, user_id = response.user.id))
        if len(todolist) > 0:
            return HttpResponse("<button id=\"change_name_form\" class=\"btn btn-danger btn-sm\" type=\"submit\" disabled>Name already existed</button>")
        elif check_for_special_character(new_name):
            return HttpResponse("<button id=\"change_name_form\" class=\"btn btn-danger btn-sm\" type=\"submit\" disabled>Contain special character</button>")
        elif len(new_name) == 0:
            return HttpResponse("<button id=\"change_name_form\" class=\"btn btn-danger btn-sm\" type=\"submit\" disabled>Please type something</button>")
        else:
            return HttpResponse("<button id=\"change_name_form\" class=\"btn btn-success btn-sm\" type=\"submit\">Save</button>")

def update_check_box(response, list_name, item_id):
    if response.method == "POST":
        now_todolist = ToDoLists.objects.get(user_id = response.user.id, name = list_name)
        now_item = Items.objects.get(todolist_id = now_todolist.id, id = item_id)
        if response.POST.get(f"checkbox_{item_id}") == None:
            now_item.complete = 0
        else:
            now_item.complete = 1
        now_item.save()
    return HttpResponse()

def check_item_name(response):
    if response.method == "POST":
        item_name = response.POST.get("new_item_name")
        if check_for_special_character(item_name):
            return HttpResponse("<button id=\"add_item_button\" class=\"add btn btn-danger font-weight-bold\" disabled>Contain special character</button>")
        elif len(item_name) > 30:
            return HttpResponse("<button id=\"add_item_button\" class=\"add btn btn-danger font-weight-bold\" disabled>Too long</button>")
        elif len(item_name) == 0:
            return HttpResponse("<button id=\"add_item_button\" class=\"add btn btn-danger font-weight-bold\" disabled>Add</button>")
        else:
            return HttpResponse("<button id=\"add_item_button\" class=\"add btn btn-primary font-weight-bold\" >Add</button>")

def update_new_item(response, list_name):
    if response.method == "POST":
        now_todolist = ToDoLists.objects.get(user_id = response.user.id, name = list_name)
        item = Items(name = response.POST.get("new_item_name"), todolist_id = now_todolist.id)
        item.save()
    return redirect(f"/todolist_{list_name}")

def delete_item(response, list_name, item_id):
    if response.method == "POST":
        now_todolist = ToDoLists.objects.get(user_id = response.user.id, name = list_name)
        item = Items.objects.get(id = item_id)
        item.delete()
    return render(response, "todolist/delete_item.html", {"now_todolist": now_todolist})