from django.conf import settings
from django.db import models
from profiles.models import User
from admin_owner.models import Blog

STATUS = (
    (0,"Send"),
    (1,"Recieve"),
    (2,"Reject"),
)




class Contact(models.Model):
    first_name=models.CharField(max_length=30)
    second_name=models.CharField(max_length=30)
    email_id=models.EmailField(max_length=254)
    message=models.CharField(max_length=150)
    status = models.IntegerField(choices=STATUS, default=0)
    mobile_no=models.CharField(max_length=12,blank=True,null=True)

    def __str__(self):
        return self.first_name


class Feedback(models.Model):
    farmer_name = models.CharField(max_length=120,help_text="Name of the sender")
    email = models.EmailField()
    title = models.ForeignKey(Blog,related_name='Feedback', on_delete=models.CASCADE,null=True)
    details = models.CharField(max_length=120,blank=True,null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.farmer_name + "-" +self.email


class Complaint(models.Model):
    name=models.CharField(max_length=40,blank=True,null=True)
    email=models.EmailField()
    date = models.DateField(auto_now_add=True)
    complaint_type=models.CharField(max_length=30,blank=True,null=True)
    complaint_message=models.CharField(max_length=200,blank=True,null=True)

