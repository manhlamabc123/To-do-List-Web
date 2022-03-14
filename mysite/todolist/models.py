from http.client import ResponseNotReady
from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages

# Create your models here.
class ToDoLists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    @staticmethod
    def UserFirstList(user_id):
        user_todolist = list(ToDoLists.objects.filter(user_id = user_id).order_by('id'))
        return user_todolist[0]

    @staticmethod
    def IsExistedTodolist(user_id, todolist_name):
        search_todolist = list(ToDoLists.objects.filter(user_id = user_id, name = todolist_name))
        if len(search_todolist) >= 1:
            return True
        return False

    @staticmethod
    def ListNameGenerator(response):
        user_todolist = list(ToDoLists.objects.filter(user_id = response.user.id))
        if len(user_todolist) >= 5:
            messages.error(response, f"You already have 5 To-do Lists. You cannot have more.")
            return None
        new_list_name = f"NewList{len(user_todolist) + 1}"
        if ToDoLists.IsExistedTodolist(response.user.id, new_list_name):
            messages.error(response, f"Cannot create to-do list because {new_list_name} is already existed.")
            return None
        else:
            messages.success(response, f"{new_list_name} is created successfully! Please change your list's name.")
            return new_list_name

    @staticmethod
    def CreateNewToDoList(response, new_todolist_name):
        new_todolist = ToDoLists(user_id = response.user.id, name = new_todolist_name)
        new_todolist.save()
        
        return None

    @staticmethod
    def DeleteTodolist(response, user_id, current_list):
        delete_todolist = ToDoLists.objects.get(user_id = user_id, name = current_list)
        delete_todolist.delete()

        user_todolist = list(ToDoLists.objects.filter(user_id = user_id))
        if len(user_todolist) == 0:
            new_list_name = ToDoLists.ListNameGenerator(response)
            ToDoLists.CreateNewToDoList(response, new_list_name)
            return new_list_name
        
        return None
class Items(models.Model):
    
    class Priority(models.IntegerChoices):
        URGENT = 3
        IMPORTANT = 2
        NORMAL = 1

    todolist = models.ForeignKey(ToDoLists, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    deadline = models.DateTimeField(null=True)
    complete = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(choices=Priority.choices, null=True)

    def __str__(self):
        return self.name