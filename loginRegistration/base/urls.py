from django.urls import path, include
from .views import  home, profile, RegisterView


urlpatterns = [
    path('', home, name="base-home"),
    path('register/', RegisterView.as_view(), name="users-register"),
    path('profile/', profile, name='user-profile'),
]