from django.urls import path, include
from .views import innovate as innovate_views
from .views import science_one as science_views_one
from .views import science_two as science_views_two
from .views import space_one as space_views_one
from .views import space_two as space_views_two
from .views import space_three as space_views_three



urlpatterns = [
    path('innovate-education',  innovate_views, name='innovate'),
    path('science-education-one',  science_views_one, name='science-1'),
    path('science-education-two',  science_views_two, name='science-2'),
    path('space-one',  space_views_one, name='space-1'),
    path('space-two',  space_views_two, name='space-2'),
    path('space-three',  space_views_three, name='space-3'),    
]