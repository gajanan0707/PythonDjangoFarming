from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

CHOICES=(
    ('surat','Surat'),
    ('pune','Pune'),
    ('mumbai','Mumbai'),
)

USER_TYPE_CHOICES=(
    ('farmer','Farmer'),
    ('dealer','Dealer'),
)

USER_GENDER=(
    ('male','Male'),
    ('female','female'),
)

class User(AbstractUser):
    dob=models.DateField(null=True, blank=True)
    city=models.CharField(max_length=40, null=True,blank=True,choices=CHOICES)
    user_type=models.CharField(max_length=8,choices=USER_TYPE_CHOICES,null=True,blank=True)
    adress=models.CharField(max_length=50,null=True,blank=True)
    pincode=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=10, null=True,blank=True,choices=USER_GENDER)