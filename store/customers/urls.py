from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import ProfileView, LoginView, SignupView

urlpatterns = [
    path("profile/<slug:slug>", ProfileView.as_view(), name="account_profile"),
    path("logout", LogoutView.as_view(), name="account_logout"),
    path("login", LoginView.as_view(), name="account_login"),
    path("signup", SignupView.as_view(), name="account_signup"),
]
