from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField('Name', max_length=20)


    def __str__(self):
        return self.name

class User(AbstractUser):
    avatars = models.ImageField(upload_to='avatars/', null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    date_of_birth = models.DateField('date_of_birth', null=True)
    REQUIRED_FIELDS = []

