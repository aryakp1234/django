from django.db import models

# Create your models here.


class Department(models.Model):
    dept=models.CharField(max_length=225)

class Hod(models.Model):
    hodname=models.CharField(max_length=255)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)

class Tutor(models.Model):
    tname=models.CharField(max_length=255)
    hodname=models.ForeignKey(Hod,on_delete=models.CASCADE)
