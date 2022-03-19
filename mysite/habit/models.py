from tracemalloc import start
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Habits(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    counter = models.PositiveSmallIntegerField(default=0)
    complete = models.BooleanField(default=False)
    start_date = models.DateField(default=datetime.now().date())

class Do(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="habit", null=True)
    habit = models.ForeignKey(Habits, on_delete=models.CASCADE)