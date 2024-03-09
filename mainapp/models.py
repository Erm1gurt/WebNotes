from django.contrib.auth import get_user_model
from django.db import models

from users.models import User


# Create your models here.

class Notes(models.Model):
    note_text = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.note_text