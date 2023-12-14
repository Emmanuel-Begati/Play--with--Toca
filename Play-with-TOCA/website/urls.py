from django.urls import path, include
from .views import home as home_views


urlpatterns = [
    path('home',  home_views, name='home'),
    path('', home_views, name='home')
]