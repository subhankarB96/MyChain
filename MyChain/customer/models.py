from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50)
    product_id=models.CharField(max_length=40, default="")
    product_quantity=models.CharField(max_length=50, default="")
    description=models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name