from django.db import models
from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     full_name = models.CharField(max_length=100, blank=True)
#     date_of_birth = models.DateField(null=True, blank=True)
#     location = models.CharField(max_length=100, blank=True)

#     # Other fields you want to add
#     bio = models.TextField(blank=True)
#     social_media_links = models.TextField(blank=True)
#     # ...

#     def __str__(self):
#         return self.username   
#         pass

