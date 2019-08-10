from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
                UserCreateView, UserDetailView,
                UserListView, user_del_view,
                UserLoginView
                )

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/del/<int:pk>/', user_del_view, name='user_delete'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
