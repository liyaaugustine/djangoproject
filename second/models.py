from django.db import models
from django.db.models import Q,F

class Login(models.Model):
    Username=models.CharField(max_length=30)
    Password=models.CharField(max_length=8)
    def __str__(self):
        return self.Username
class UserDetails(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    date=models.DateField()
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
    place=models.CharField(max_length=30)
    parentname=models.CharField(max_length=30)
    phone=models.BigIntegerField()
class Contact(models.Model):
    phone=models.BigIntegerField()
    user=models.OneToOneField(Login,on_delete=models.CASCADE)  
class Publication(models.Model):
    title=models.CharField(max_length=30)
class Article(models.Model):
    headline=models.CharField(max_length=100)
    publications=models.ManyToManyField(Publication)
class MyLogin(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=10)

class Admission(models.Model):
    email=models.EmailField(max_length=100)
    candidatename=models.CharField(max_length=50)
    parentname=models.CharField(max_length=50)
    phonenumber=models.BigIntegerField()
    category=models.CharField(max_length=50)
    application=models.CharField(max_length=100)
    sslc=models.FileField(upload_to='certificates/')
    plus2=models.FileField(upload_to='certificates/')
    degree=models.FileField(upload_to='certificates/')
    qualification=models.CharField(max_length=100)



    
