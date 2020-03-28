from django.db import models
from django.contrib.auth.models import User

class Ram(models.Model):
    full_name=models.CharField(max_length=100)
    national_id=models.CharField(max_length=8)
    phone_number=models.CharField(max_length=10)
    gender=models.CharField(max_length=50)
    vehicle_name=models.CharField(max_length=40)
    vehicle_number=models.CharField(max_length=13)
    date=models.DateField()
    entry_time=models.CharField(max_length=7)
    exit_time=models.CharField(max_length=7)

class Gatepassuser(models.Model):
     user=models.OneToOneField(User,on_delete="models.CASCADE")
     nickname=models.CharField(max_length=20,null=False)
