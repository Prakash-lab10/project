# myapp/urls.py

from django.urls import path
from .views import feed, create_message, create_comment, like_message, delete_message

urlpatterns = [
    path('feed/', feed, name='feed'),
    path('create_message/', create_message, name='create_message'),
    path('create_comment/<int:message_id>/', create_comment, name='create_comment'),
    path('like_message/<int:message_id>/', like_message, name='like_message'),
    path('delete_message/<int:message_id>/', delete_message, name='delete_message'),
]
