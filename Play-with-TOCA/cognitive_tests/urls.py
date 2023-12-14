from django.urls import path, include
from .views import cognitive as cognitive_views
from .views import visual as visual_views
from .views import questions as questions_views


urlpatterns = [
    path('cognitive',  cognitive_views, name='cognitive'),
    path('questions', questions_views, name='questions' ),
    path('visual', visual_views, name='visual')
]