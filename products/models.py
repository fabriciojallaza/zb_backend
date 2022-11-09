from django.db import models


# Create your models here.
class Product(models.Model):
    sku = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #created_by = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='products')
    #updated_by = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='+')
