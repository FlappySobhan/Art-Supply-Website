from django.shortcuts import render, redirect
from django.views.generic import DetailView,CreateView,View
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login, authenticate
User = get_user_model()

from .models import Profile
from .forms import SignupForm, LoginForm

class ProfileView(DetailView):
    model = User
    template_name = "account/profile.html"
    context_object_name = "logged_in_user"

    def get_object(self, *args, **kwargs):
        user = super().get_object()
        self.profile = Profile.objects.get(user=user)
        if user == self.request.user or self.request.user.is_superuser:
            return user
        else:
            messages.error(self.request, "You don't have permission to view this page")
            return redirect("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.profile
        return context

class SignupView(CreateView):
    form_class = SignupForm
    success_url = "account_login"
    template_name = "account/signup.html"
    
    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Account created successfully")
        return redirect("account_login")

class LoginView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            messages.error(self.request, "You are already logged in")
            return redirect("profile")
        return render(self.request, "account/login.html", {"form": LoginForm()})

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST or None)
        if form.is_valid():
            login = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            try:
                user = User.objects.get(phone_number=login)
            except User.DoesNotExist:
                messages.error(self.request, "Invalid login or password")
                return redirect("account_login")

            if user.check_password(password):
                auth_login(self.request, user)
                messages.success(self.request, "You have successfully logged in")
                if not remember:
                    self.request.session.set_expiry(0)
                    # self.request.session.modified = True
                return redirect("account_profile", slug=user.slug)
                
        
        messages.error(self.request, "Check login and password!")
        return redirect("account_login")