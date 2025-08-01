from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
# previous login url
     path('login/', views.user_login, name='login'),
]