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

class StudentLogin(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=8)

class Admission(models.Model):
    usertype=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)#this remove
    candidatename=models.CharField(max_length=50)
    parentname=models.CharField(max_length=50)
    phonenumber=models.BigIntegerField()
    category=models.CharField(max_length=50)
    application=models.CharField(max_length=100)
    sslcmark=models.CharField(max_length=10)
    plus2mark=models.CharField(max_length=10)
    ugmark=models.CharField(max_length=10)
    sslc=models.FileField(upload_to='certificates/')
    plus2=models.FileField(upload_to='certificates/')
    degree=models.FileField(upload_to='certificates/')
    qualification=models.CharField(max_length=100)
    logid=models.ForeignKey(StudentLogin,on_delete=models.CASCADE)
class Degree(models.Model):
    usertype=models.CharField(max_length=20)
    email=models.EmailField(max_length=100)# remove this field from 2 table 
    candidatename=models.CharField(max_length=50)
    parentname=models.CharField(max_length=50)
    phonenumber=models.BigIntegerField()
    category=models.CharField(max_length=50)
    application=models.CharField(max_length=100)
    sslcmark=models.CharField(max_length=10)
    plus2mark=models.CharField(max_length=10)
    sslc=models.FileField(upload_to='certificates/')
    plus2=models.FileField(upload_to='certificates/')
    qualification=models.CharField(max_length=100)
    logid=models.ForeignKey(StudentLogin,on_delete=models.CASCADE)

class Count(models.Model):
    student=models.CharField(max_length=20)
    teacher=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    loginid=models.ForeignKey(MyLogin,on_delete=models.CASCADE)
class Event(models.Model):
    day=models.CharField(max_length=15)
    event=models.CharField(max_length=30)
    loginid=models.ForeignKey(MyLogin,on_delete=models.CASCADE)
class Month(models.Model):
    month=models.CharField(max_length=10)
    loginid=models.ForeignKey(MyLogin,on_delete=models.CASCADE)
class ContactDetails(models.Model):
    address=models.TextField()
    email=models.EmailField(max_length=100)
    firstnum=models.BigIntegerField()
    secnum=models.BigIntegerField()
    loginid=models.ForeignKey(MyLogin,on_delete=models.CASCADE)
class Image(models.Model):
    images=models.FileField(upload_to='certificates/')
    loginid=models.ForeignKey(MyLogin,on_delete=models.CASCADE)
    
class Message(models.Model):
    studentname=models.CharField(max_length=50)
    mail=models.EmailField(max_length=100)
    contact=models.BigIntegerField()
    message=models.TextField() 
    status=models.CharField(max_length=20,default='active') 
class Reply(models.Model):
    reply=models.TextField()
    loginid=models.ForeignKey(MyLogin,on_delete=models.CASCADE)
    mesageid=models.ForeignKey(Message,on_delete=models.CASCADE)
class UgAcademics(models.Model):
    subjects=models.CharField(max_length=30)
    fees=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=30)
    job=models.TextField()
    loginid=models.ForeignKey(MyLogin,on_delete=models.CASCADE)
class PgAcademics(models.Model):
    subjects=models.CharField(max_length=30)
    fees=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=30)
    job=models.TextField()
    loginid=models.ForeignKey(MyLogin,on_delete=models.CASCADE) 







    
