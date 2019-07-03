from django.db import models

class profile(models.Model):
    Name=models.CharField(max_length=50,null=False)
    Email=models.EmailField(null=False)
    #Username=models.CharField(max_length=50,null=False)
    Contect=models.IntegerField()
    Designation=models.CharField(max_length=50,choices=[('a','student'),('b','professional'),('c','other')])
    Organisation=models.CharField(max_length=50,null=False)
    Address=models.TextField()
    Bio=models.TextField()

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

    def _str_(self):
        return self.Title

class payment(models.Model):
    Transaction_id=models.IntegerField()
    Transaction_status=models.CharField(max_length=50)

    def _str_(self):
        return self.Transaction_id


class Notification(models.Model):
    message=models.TextField()

    def _str_(self):
        return self.message



# Create your models here.
