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
    # once a person performs this action, this is where they'll be redirected
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        # checking if a group exists
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            # create user-group link using GroupMember model
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(
                self.request,
                "Warning, already a member of {}.".format(group.name)
            )
        else:
            messages.success(
                self.request,
                "You are now a member of the {} group.".format(group.name)
            )

        return super().get(request, *args, **kwargs)

class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
    # once a person performs this action, this is where they;ll be redirected
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            membership = models.GroupMember.objects.filter(
                user = self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()

        except models.GroupMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave {} group because you're not a member!".format(group.name)
            )
        else:
            membership.delete()
            messages.success(
                self.request,
                "You've successfully left {} group.".format(group.name)
            )

        return super().get(request,*args, **kwargs)
