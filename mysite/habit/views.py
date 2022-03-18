from django.shortcuts import render

# Create your views here.
def habit(response):
    return render(response, "habit/habit.html", {})