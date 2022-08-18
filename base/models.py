
from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser


class User (AbstractUser):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)


class Todo(models.Model):
    tag = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.tag
