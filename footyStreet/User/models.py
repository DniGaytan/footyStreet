from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserExtra(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)
    name = models.CharField(max_length = 50)
    bornDate = models.DateField()
