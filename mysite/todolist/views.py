from django.contrib import messages
from django.http import HttpRequest, HttpResponse
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

def clicked_todolist_name(response):
    replace_with = '''<div 
                        class="card-header-title font-size-lg text-capitalize font-weight-normal"
                    ><i class=\"fa fa-tasks\"></i>&nbsp;
                        <form action=\"/edit_todolist_name\">\n
                            <div class=\"input-group input-group-sm\">\n
                                <input type=\"text\" class=\"form-control\" placeholder=\"New name\" name="new_name">\n
                                <button 
                                    class=\"btn btn-primary btn-sm\" 
                                    type=\"button\"
                                >Save</button>\n
                            </div>\n
                        </form>
                    </div>'''
    return HttpResponse(replace_with)

def edit_todolist_name(response):
    if response.method == "POST":
        new_name = response.POST.get("new_name")
        print(new_name)
    return HttpResponse(new_name)