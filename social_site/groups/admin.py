from django.contrib import admin
from . import models

# Register your models here.

# use admin interface to edit models on the same page as the parent model
# no need to register it, 
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

# naming convention: ModelClass+Admin
class GroupAdmin(admin.ModelAdmin):
    fields = ['name','description', 'slug']

admin.site.register(models.Group, GroupAdmin)