from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from register.forms import NewUserForm, UpdateUserForm, PasswordChangingForm
from django.contrib.auth.forms import AuthenticationForm
from todolist.models import ToDoLists
from django.contrib.auth.views import PasswordChangeView
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

def profile(response):
    user = response.user
    return render(response, "register/profile.html", {"user": user})

def edit_profile(response):
    if response.method == "GET":
        user_form = UpdateUserForm(instance=response.user)
        return render(response, "register/edit_profile.html", {"form": user_form})
    else:
        user_form = UpdateUserForm(response.POST, instance=response.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(response, 'Your profile is updated successfully')
            return redirect("profile")
        else:
            messages.error(response, 'Error! Please check your input again.')
            return redirect("edit_profile")

class PasswordsChangeView(PasswordChangeView):
	form_class = PasswordChangingForm
	success_url = reverse_lazy('profile')