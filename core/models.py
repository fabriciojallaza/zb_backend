from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """Creates and saves a new user
        :param username: str username
        :param password: str password
        :param extra_fields: dict extra fields
        :return: object user
        """
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model, if is_staff is True, user is admin"""
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=128)
    is_active = models.IntegerField(default=1)
    date_joined = models.DateTimeField(editable=False, auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

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
    visits = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    # created_by = models.ForeignKey('user.models', on_delete=models.CASCADE, related_name='products')
    # updated_by = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.sku
