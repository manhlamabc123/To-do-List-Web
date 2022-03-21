from django.urls import path
from register import views
from django.views.generic.base import TemplateView
urlpatterns = [
    path('register/', views.register_request, name = "register"),
    path('login/', views.login_request, name = "login"),
    path('logout/', views.logout_request, name = "logout"),
    path("", TemplateView.as_view(template_name = "home.html"), name = "home")
]
 