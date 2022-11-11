from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        """Creates and saves a new user
        :param email: str email
        :param username: str username
        :param password: str password
        :param extra_fields: dict extra fields
        :return: object user
        """
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        self.create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model, if is_staff is True, user is admin"""
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=256)
    is_active = models.IntegerField(default=1)
    date_joined = models.DateTimeField(editable=False, auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

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

    def __str__(self):
        return self.sku
