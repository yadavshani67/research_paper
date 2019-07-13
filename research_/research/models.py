from django.contrib import admin 
from django.contrib.auth.models import User 
from django.db import models 
from django.conf import settings

User=settings.AUTH_USER_MODEL

class profile(models.Model):
    user=models.CharField(max_length=50,null=True)
    Name=models.CharField(max_length=50,null=False)
    Email=models.EmailField(null=False)
    #Username=models.CharField(max_length=50,null=False)
    Contect=models.IntegerField()
    Designation=models.CharField(max_length=50,choices=[('a','student'),('b','professional'),('c','other')])
    Organisation=models.CharField(max_length=50,null=False)
    Address=models.TextField()
    Bio=models.TextField()
    #user=models.OneToOneField(User,null=True, on_delete=models.CASCADE) 

    def _str_(self):
        return self.Name

class paper(models.Model):
    Title=models.CharField(max_length=50,null=False)
    Research_field=models.CharField(max_length=50,null=False)
    paper_type=models.CharField(max_length=50,null=False)
    attachment=models.FileField(upload_to='documents/')
    Keywords=models.TextField()
    Author=models.TextField()
    Created_date=models.DateTimeField(auto_now =True)
    updated_date=models.DateTimeField(auto_now_add =True)
    status=models.CharField(max_length=50)
    profil=models.ForeignKey(profile,null=True, on_delete=models.CASCADE)
    user=models.CharField(max_length=50,null=True)
    #user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    def _str_(self):
        return self.Title


class payment(models.Model):
    #paper_no=models.ForeignKey(paper,on_delete=models.CASCADE)
    Transaction_id=models.IntegerField()
    Transaction_status=models.CharField(max_length=50)

    def _str_(self):
        return self.Transaction_id


class Notification(models.Model):
    #paper_no=models.ForeignKey(paper,on_delete=models.CASCADE)
    #status=models.CharField(max_length=50)
    message=models.TextField()

    def _str_(self):
        return self.message



# Create your models here.
