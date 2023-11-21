from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=200)
    password=models.TextField(max_length=200)
    confirmpassword=models.TextField(max_length=200)
    name = models.TextField(max_length=200)
    dob = models.DateField(max_length=200)
    age = models.IntegerField(max_length=200)
    gender = models.CharField(max_length=200)
    phonenumber = models.IntegerField()
    mailid = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    purpose = models.CharField(max_length=200)
    materialprovides = models.CharField(max_length=200)
