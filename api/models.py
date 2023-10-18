from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=500)
    tel = models.CharField(max_length=500)
    age = models.CharField(max_length=500)