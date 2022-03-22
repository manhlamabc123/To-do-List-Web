from django.urls import path
from register import views
from django.views.generic.base import TemplateView
from .views import PasswordsChangeView

urlpatterns = [
    path('register/', views.register_request, name = "register"),
    path('login/', views.login_request, name = "login"),
    path('logout/', views.logout_request, name = "logout"),
    path('profile/', views.profile, name = "profile"),
    path('edit_profile/', views.edit_profile, name = "edit_profile"),
    path('change_password/', PasswordsChangeView.as_view(template_name='register/change_password.html')),
    path("", TemplateView.as_view(template_name = "home.html"), name = "home")
]
 