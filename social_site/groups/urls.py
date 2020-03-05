from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    # when someone goes to website/groups, this is what they'll see first
    path('', views.ListGroup.as_view(), name='all'),
    path('new/', views.CreateGroup.as_view(), name='create'),
    # when a loged user wants to see all posts in a single group:
    path('posts/in/<slug>/', views.SingleGroup.as_view(), name='single'),
]
