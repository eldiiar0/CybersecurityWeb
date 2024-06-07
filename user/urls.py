from django.urls import path

from .views import *
from django.contrib.auth import views as auth_views


app_name = 'user'
urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home:home_page'), name='logout'),
]

