# Django imports
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login, logout
# app imports
from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    # if it was reverse(), users would be automatically reversed, before hitting submit button
    template_name = 'accounts/signup.html'

