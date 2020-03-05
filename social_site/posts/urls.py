from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # default view, when you go to /posts/
    path('', views.PostList.as_view(), name = 'all'),
    path('new/', views.CreatePost.as_view(), name = 'create'),
    # use this to see all posts created by an user
    path('by/<username>/', views.UserPosts.as_view(), name = 'for_user'),
    path('by/<username>/<int:pk>/', views.PostDetail.as_view(), name = 'single'),
    path('delete/<int:pk>/', views.DeletePost.as_view(), name = 'delete'),
]
