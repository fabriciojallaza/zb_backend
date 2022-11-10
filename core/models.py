import re
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Model to for customize users model
class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.email = self.normalize_email(email)
        user.set_password(password)  # Encrypt password
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_active = models.IntegerField(default=1)
    date_joined = models.DateTimeField(editable=False, auto_now_add=True)

    objects = UserManager()
    #get_email_field_name()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username


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
