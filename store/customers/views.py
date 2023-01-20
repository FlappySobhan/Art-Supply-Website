from django.shortcuts import render, redirect
from django.views.generic import DetailView,CreateView
from django.contrib import messages
from django.contrib.auth import  get_user_model
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.mixins import PermissionRequiredMixin,UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import resolve_url
from django.http import Http404
from django.urls import reverse_lazy as _

User = get_user_model()

from .forms import SignupForm, LoginForm

class ProfileView(PermissionRequiredMixin, DetailView):
    model = User
    template_name = "account/profile.html"
    context_object_name = "logged_in_user"
    permission_denied_message = _("You don't have permission to view this page.Check your account!")
    login_url = "account_login"
    

    def has_permission(self):
        if self.get_object() == self.request.user or self.request.user.is_superuser:
            return True
        return False

    def handle_no_permission(self):
        try:
            object = super().handle_no_permission()
        except PermissionDenied:
            messages.error(self.request, self.get_permission_denied_message())
            return redirect("account_login")
        return object

    def get_object(self, *args, **kwargs):
        try:
            user = super().get_object()
        except Http404:
            messages.error(self.request, "User not found!")
            return redirect("account_login") 
        return user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_object().profile
        return context

class SignupView(UserPassesTestMixin, CreateView):
    form_class = SignupForm
    success_url = "account_login"
    template_name = "account/signup.html"
    prrmisson_denied_message = _("You are already logged in!")
    
    def test_func(self):
        return self.request.user.is_anonymous

    def handle_no_permission(self):
        try:
            object = super().handle_no_permission()
        except PermissionDenied:
            messages.error(self.request, self.get_permission_denied_message())
            return redirect("account_login")
        return object

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, _("Account created successfully"))
        return redirect("account_login")

class LoginView(BaseLoginView):
    next_page = "account_profile"
    next_page_arg = 'slug'
    template_name = "account/login.html"
    form_class = LoginForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        valid_form=super().form_valid(form)
        remember = form.cleaned_data.get('remember')
        if not remember:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return valid_form

    def get_default_redirect_url(self):
        """Return the default redirect URL."""
        return resolve_url(self.next_page, getattr(self.request.user,self.next_page_arg))
    