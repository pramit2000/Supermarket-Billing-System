from django.db import models
from enum import Enum

# Create your models here.
class emp_reg(models.Model):

    class genderEnum(models.TextChoices):
        m = 'Male'
        f = 'Female'
        o = 'Other'

    email_id = models.EmailField(primary_key= True)
    fullname = models.CharField(max_length=30)
    gender = genderEnum.choices
    dateOfBirth = models.DateField()
    contact_no = models.IntegerField(max_length=10)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    pin_code = models.IntegerField(max_length=6)
    emp_id = models.IntegerField(auto_created=True)


class emp_login(models.Model):
    email_id = models.EmailField()
    password = models.ForeignKey(emp_reg, on_delete=models.CASCADE)