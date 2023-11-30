from django.db import models

# Create your models here.
class Mobile(models.Model):
    task=models.CharField(max_length=255)