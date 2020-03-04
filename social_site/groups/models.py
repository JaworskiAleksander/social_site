from django.db import models
from django.utils.text import slugify   # allows to remove unwanted characters


# Create your models here.
import misaka
from django.contrib.auth import get_user_model  # this method returns user model that's actually in use
User = get_user_model()

# this is how we use custom template tags
from django import template
register = template.Library()

class Group(models.Model):
    pass

class GroupMember(models.Model):
    pass