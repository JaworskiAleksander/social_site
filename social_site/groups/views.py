# django imports
from django.shortcuts import render

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib import messages

# app imports
from groups.models import Group, GroupMember
from . import models



# when someone logged in the system wants to create a group ...
# login required + createview
class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name','description') # only those fields will be shown with a form tag
    model = Group # this model will be used to store data in db.sqlite3

# display detailed information about a group - posts, members, et c.
class SingleGroup(generic.DetailView):
    model = Group

class ListGroup(generic.ListView):
    model = Group

# in order to join a group, you have to be loged in
class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    # checking if user is already a member of this group
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request,"Warning, already a member of {}".format(group.name))
        else:
            messages.success(self.request, "You are now a member of the {} group".format(group.name))

        return super().get(request, *args, **kwargs)

class LeaveGroup():
    pass
