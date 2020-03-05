from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404

# braces take care of using mixins
from braces.views import SelectRelatedMixin

from . import models
from . import forms

# when someone is logged in a session, I'm able to use it as a current user object and do stuff with that
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
# show all posts
class PostList(LoginRequiredMixin, generic.ListView):
    model = models.Post
    # a mixin, that allows to provide a tuple of a related model, a foreign key for this post
    select_related = ('user', 'group')

# show all posts created by that user
class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'post/user_list_view.html'

    def get_queryset(self):
        try:
            # from User that is currently viewing their posts (line 15+16)
            # get all objects related to "post", and from those grab all that
            # match username
            self.post_user = User.objects.prefetch_related("posts").get(
                username__isexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context

