import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""
    username = models.CharField(unique=True, max_length=150)
    email = models.EmailField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


class Product(models.Model):
    """Product Model"""
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    brand = models.CharField(max_length=200)
