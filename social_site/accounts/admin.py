from django.contrib import admin
from . import models

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields=['username']

admin.site.register(models.User, UserAdmin)