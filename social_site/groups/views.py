from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.urls import reverse
from django.db import IntegrityError
from django.views import generic
from . import models



# when someone logged in the system wants to create a group ...
# login required + createview
class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name','description') # those fields will be shown with a form tag
    model = Group # this model will be used to store data in db.sqlite3

