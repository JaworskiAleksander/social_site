from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.
import misaka

from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    # User model is known thanks to get_user_model; django takes care of that for us!
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

# get absolute url - when someone posts something, this is where they'll be sent through
    # methods
    def __str__(self):
        return self.user.username + "@" + self.group.name + ' : ' + self.message

    # when someone writes using markdown or posts a link, it gets properly supported
    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'posts:single',
            kwargs={
                'username': self.user.username,
                'pk': self.pk
            }
        )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message'] # this can also be a tuple; every message is uniquely linked to a user
    
    
    
