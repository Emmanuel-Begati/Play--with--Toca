from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import signup as signup_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path ('signup', signup_views, name='sign-up'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]