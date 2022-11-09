import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Product(models.Model):
    """Product model"""
    sku = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    brand = models.CharField(max_length=255)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(null=True)
    # created_by = models.ForeignKey('user.models', on_delete=models.CASCADE, related_name='products')
    # updated_by = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='+')
    visits = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.sku
