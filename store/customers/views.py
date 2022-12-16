from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileUpdateForm
from .models import Profile
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

class ProfileView(View):
    model = Profile
    template_name = "account/profile.html"

    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        # u_form = CustomUserChangeForm(instance=request.user)
        # p_form = ProfileUpdateForm(instance=profile)
        context = {
            'profile': profile,
        }
        return render(request, self.template_name, context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["profile"] = Profile.objects.get(user=self.request.user)
    #     return context


# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created! You are now able to log in')
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'users/register.html', {'form': form})
 

# @login_required
# def profile(request):
    # if request.method == 'POST':
    #     profile = Profile.objects.get(user=request.user)
    #     u_form = CustomUserChangeForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST,
    #                                request.FILES,
    #                                instance=profile)
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, f'Your account has been updated!')
    #         return redirect('profile')
 
    # else:
    #     u_form = CustomUserChangeForm(instance=request.user)
    #     p_form = ProfileUpdateForm(instance=profile)
 
    # context = {
    #     'u_form': u_form,
    #     'p_form': p_form
    # }
 
    # return render(request, 'account/profile.html', context)