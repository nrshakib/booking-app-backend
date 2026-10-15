from django.urls import path
from user import views

urlpatterns = [
    path('', views.api_root, name='auth'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetails.as_view(), name='user-details'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
]