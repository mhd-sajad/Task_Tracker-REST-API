from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings 


class CustomUser(AbstractUser):

    bio = models.TextField(blank=True)
    dob = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.username

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
