from django.db import models

# Create your models here.

class reg(models.Model):
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    confirmpassword=models.CharField(max_length=255)

class log(models.Model):
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

class head(models.Model):
    name=models.CharField(max_length=255)
    image=models.ImageField(upload_to="pics")
    discription=models.CharField(max_length=255)
class con(models.Model):
    name=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)

class boo(models.Model):
    Address=models.CharField(max_length=255)
    number=models.CharField(max_length=255)