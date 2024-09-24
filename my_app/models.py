

from django.db import models
from django.utils import timezone

from users.models import User


# Create your models here.

class Note(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField('Description')
    done = models.BooleanField('done', default=False)
    created_at = models.DateTimeField('created_at', auto_now_add=True)


    def __str__(self):
        return self.name



