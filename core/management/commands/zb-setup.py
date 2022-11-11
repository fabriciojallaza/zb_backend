from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import make_aware
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from core.models import Product


class Command(BaseCommand):
    help = "Creates a superuser and populated db"

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)
        self.client = None
        self.user = None

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        # User creation
        self.user = get_user_model()
        self.user.objects.create_superuser(username='admin_user', email='admin_user@zb.com', password='admin_pass123',
                                           date_joined=make_aware(datetime.now()))
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        print("User created")
        # Products creation
        Product.objects.create(sku='PROD-1', name='Razer Vyper', price=55.77, brand='Razer',
                               created_at=make_aware(datetime.now()))
        Product.objects.create(sku='PROD-2', name='Razer Kraken', price=20.0, brand='Razer',
                               created_at=make_aware(datetime.now()))
        Product.objects.create(sku='PROD-3', name='Razer Headphones', price=66.88, brand='Razer',
                               created_at=make_aware(datetime.now()))
        Product.objects.create(sku='PROD-4', name='Razer Mouse', price=99.99, brand='Razer',
                               created_at=make_aware(datetime.now()))
        print('Database populated')
