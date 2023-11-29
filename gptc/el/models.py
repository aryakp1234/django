from django.db import models

# Create your models here.

class Student (models.Model):
    name=models.CharField(max_length=255)
    Rno=models.IntegerField()

class Teacher (models.Model):
    name=models.CharField(max_length=255)
    sub=models.CharField(max_length=255)



