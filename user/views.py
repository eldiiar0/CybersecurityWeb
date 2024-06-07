from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login

from .forms import *


# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:home_page')
    else:
        form = RegistrationForm()
    return render(request, 'user/registration.html', {'form': form})
    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save(commit=False)
    #         form.save()
    #         user = form.cleaned_data.get('username')
    #         messages.success(request, 'Account was created for ' + user)
    #         return redirect('user:login')
    # else:
    #     form = RegistrationForm()

    # return render(request, 'user/registration.html', {form:'form'})


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    authentication_form = LoginForm

    def get_success_url(self):
        return reverse_lazy('members_area:member_page') 
    