from django.db import models
from enum import Enum

# Create your models here.
class emp_reg(models.Model):

    email_id = models.EmailField(primary_key= True)
    fullname = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, default='Male')
    dateOfBirth = models.DateField()
    contact_no = models.IntegerField()
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    pin_code = models.IntegerField()
    emp_id = models.IntegerField(auto_created=True)


class emp_login(models.Model):
    email_id = models.ForeignKey(emp_reg, on_delete=models.CASCADE)
    password = models.CharField(max_length=15)