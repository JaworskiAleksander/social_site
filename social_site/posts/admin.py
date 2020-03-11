from django.contrib import admin
from . import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    search_fields = ['user']
    list_filter = ['group', 'user']
    list_display = ['user', 'group', 'message']

admin.site.register(models.Post, PostAdmin)