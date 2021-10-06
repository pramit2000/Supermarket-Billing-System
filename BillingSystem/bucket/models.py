from django.db import models

# Create your models here.
class products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=30)
    price = models.FloatField(max_length=7)
    tax = models.FloatField(max_length=3,default=0.0)
    description = models.CharField(max_length=70,blank=True)
    

    def __str__(self):
        return self.product_name 