from tokenize import Pointfloat
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoLists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Items(models.Model):
    
    class Priority(models.IntegerChoices):
        URGENT = 3
        IMPORTANT = 2
        NORMAL = 1

    todolist = models.ForeignKey(ToDoLists, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    deadline = models.DateTimeField(null=True)
    complete = models.BooleanField(null=True)
    priority = models.PositiveSmallIntegerField(choices=Priority.choices, null=True)

    def __str__(self):
        return self.name