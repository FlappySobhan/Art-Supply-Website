from django.urls import path
from .views import ProfileView, LoginView, SignupView 
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("profile", ProfileView.as_view(), name="account_profile"),
    path("logout", LogoutView.as_view(), name="account_logout"),
    path("login", LoginView.as_view(), name="account_login"),
    path("signup", SignupView.as_view(), name="account_signup"),
]
