from django.shortcuts import render

# Create your views here.
def todolist(response):
    return render(response, "todolist/todolist.html", {})