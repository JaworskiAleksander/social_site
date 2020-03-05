from django.contrib import admin
from . import models

# Register your models here.

# use admin interface to edit models on the same page as the parent model
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)