from django.urls import path
from .views import UserListView

urlpatterns = [
    path('registration/', UserListView.as_view(), name='user-list'),
]