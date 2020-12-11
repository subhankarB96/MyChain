from django.db import models

# Create your models here.
class Supplied_list(models.Model):
    Supplier_name=models.CharField(max_length=50)
    product_id=models.CharField(max_length=50)
    product_quantity=models.CharField(max_length=50)
    description=models.CharField(max_length=300, default="")
    def __str__(self):
        return self.Supplier_name

class Requiredlist(models.Model):
    supplier_name=models.CharField(max_length=50, default="")
    product_id=models.CharField(max_length=50)
    Product_name=models.CharField(max_length=50,default="")
    product_quantity=models.CharField(max_length=50,default="")
    description=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.supplier_name 