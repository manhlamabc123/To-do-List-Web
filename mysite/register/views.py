from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from register.forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from todolist.models import ToDoLists
# Create your views here.

def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            list = ToDoLists(name = ToDoLists.ListNameGenerator(request, True), user_id = user.id)
            list.save()
            login(request, user)
            messages.success(request, "Registered successfully!")
            return redirect('/login')
        messages.error(request, "Registered failed!")
    form = NewUserForm()
    return render(request, 'register/register.html', {"register_form":form})
    
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'register/login.html', {"login_form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/login')