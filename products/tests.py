from datetime import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from django.utils.timezone import make_aware
from rest_framework import status
from rest_framework.test import APIClient
from unittest import mock
from core.models import Product
from products.serializers import ProductSerializer

PRODUCT_CREATEURL = reverse('products:product_create')


def control_producturl(pk):
    """Returns product unique url"""
    return reverse('products:product_control', args=[pk])


def view_producturl(pk=1):
    """Returns product unique url for anonymous users"""
    return reverse('products:product_view', args=[pk])


class ProductsAnonTests(TestCase):
    """Tests for products api for anonymous users"""

    def setUp(self):
        self.client = APIClient()

    def test_viewproducts_success(self):
        """Tests that products are listed for anonymous users"""
        Product.objects.create(sku='PROD-1', name='Razer Vyper', price=55.77, brand='Razer',
                               created_at=make_aware(datetime.now()))
        Product.objects.create(sku='PROD-2', name='Razer Kraken', price=20.0, brand='Razer 2',
                               created_at=make_aware(datetime.now()))
        result = self.client.get(reverse('products:products'))
        serializer = ProductSerializer(Product.objects.all(), many=True)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data, serializer.data)

    def test_viewsingleproduct_success(self):
        """Tests single product view for anonymous users"""
        product = Product.objects.create(sku='PROD-1', name='Razer Vyper', price=55.77, brand='Razer',
                                         created_at=make_aware(datetime.now()))
        result = self.client.get(view_producturl(product.id))
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['sku'], product.sku)
        self.assertEqual(result.data['name'], product.name)
        self.assertEqual(float(result.data['price']), product.price)
        self.assertEqual(result.data['brand'], product.brand)

    def test_createproduct_noauth_fail(self):
        """Tests that unauthorized users cannot create products"""
        payload = {
            'sku': 'PROD-1',
            'name': 'Razer Vyper',
            'price': 55.77,
            'brand': 'Razer',
        }
        result = self.client.post(PRODUCT_CREATEURL, payload)
        self.assertEqual(result.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_partialupdateprod_noauth_fail(self):
        """Tests that unauthorized users cannot PATCH products"""
        product = Product.objects.create(sku='PROD-1', name='Razer Vyper', price=55.77, brand='Razer',
                                         created_at=make_aware(datetime.now()))
        payload = {
            'sku': 'PROD-1',
            'name': 'Razer Vyper',
            'price': 55.77,
            'brand': 'Razer',
        }
        result = self.client.patch(control_producturl(product.id), payload)
        self.assertEqual(result.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_completeupdateprod_noauth_fail(self):
        """Tests editing a product with PUT method fails for unauthorized users"""
        product = Product.objects.create(sku='PROD-1', name='Razer Vyper', price=55.77, brand='Razer',
                                         created_at=make_aware(datetime.now()))
        payload = {
            'sku': 'PROD-1',
            'name': 'Razer Vyper',
            'price': 55.77,
            'brand': 'Razer',
        }
        result = self.client.put(control_producturl(product.id), payload)
        self.assertEqual(result.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_deleteprod_noauth_fail(self):
        """Tests that unauthorized users cannot delete products"""
        product = Product.objects.create(sku='PROD-1', name='Razer Vyper', price=55.77, brand='Razer',
                                         created_at=make_aware(datetime.now()))
        result = self.client.delete(control_producturl(product.id))
        self.assertEqual(result.status_code, status.HTTP_401_UNAUTHORIZED)


class ProductAdminTests(TestCase):
    """Tests for products api for admin users"""
    def setUp(self):
        self.user = get_user_model().objects.create_user('user_test', 'pass123')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_createproduct_success(self):
        """Tests that admin users can create products"""
        payload = {
            'sku': 'PROD-1',
            'name': 'Razer Vyper',
            'price': 55.77,
            'brand': 'Razer',
        }
        result = self.client.post(PRODUCT_CREATEURL, payload)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.data['sku'], payload['sku'])
        self.assertEqual(result.data['name'], payload['name'])
        self.assertEqual(float(result.data['price']), payload['price'])
        self.assertEqual(result.data['brand'], payload['brand'])

    def test_createproduct_duplicatesku_fail(self):
        """Tests that admin users cannot create products with duplicate sku"""
        payload = {
            'sku': 'PROD-1',
            'name': 'Razer Vyper',
            'price': 55.77,
            'brand': 'Razer',
        }
        Product.objects.create(sku='PROD-1', name='Razer Vyper', price=55.77, brand='Razer', created_at=make_aware(datetime.now()))
        response = self.client.post(PRODUCT_CREATEURL, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partialupdateprod_invalidid_fail(self):
        """Tests that admin users cannot PATCH products with invalid id"""
        Product.objects.create(sku='PROD-1', name='Razer Vyper', price=55.77, brand='Razer', created_at=make_aware(datetime.now()))
        payload = {'sku': 'PROD-NEW', 'price': 55.77, 'brand': 'Logitech'}
        response = self.client.patch(control_producturl(2), payload)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_parcialupdateprod_success(self):
        """Test updating a product with PATCH"""
        # Create a dummy product
        product = Product.objects.create(sku='PROD-1', name='Razer Vyper', price=55.77, brand='Razer', created_at=make_aware(datetime.now()))
        payload = {'name': 'Logitech Mouse', 'brand': 'Logitech'}
        with mock.patch('products.serializers.email_handler', return_value=True):   # Mock email handler to avoid spam email sending
            self.client.patch(control_producturl(product.id), payload)
        product.refresh_from_db()
        self.assertEqual(product.name, payload['name'])
        self.assertEqual(product.brand, payload['brand'])

    def test_completeupdateprod_fewparameters_fail(self):
        """Tests that admin users cannot update products with PUT method with missing parameters"""
        product = Product.objects.create(sku='PROD-1', name='Razer Vyper', price=55.77, brand='Razer', created_at=make_aware(datetime.now()))
        payload = {'sku': 'PROD-NEW', 'price': 33.33, 'brand': 'Logitech'}
        response = self.client.put(control_producturl(product.id), payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_completeupdateprod_invalidid_fail(self):
        """Tests that admin users cannot update products with PUT method with invalid id"""
        Product.objects.create(sku='PROD-1', name='Razer Vyper', price=55.77, brand='Razer', created_at=make_aware(datetime.now()))
        payload = {'sku': 'PROD-NEW', 'price': 33.33, 'brand': 'Logitech'}
        response = self.client.put(control_producturl(2), payload)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_deleteproduct_invalidid_fail(self):
        """Tests that admin users cannot delete products with invalid id"""
        Product.objects.create(sku='PROD-1', name='Razer Vyper', price=55.77, brand='Razer', created_at=make_aware(datetime.now()))
        response = self.client.delete(control_producturl(2))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_completeupdateprod_success(self):
        """Tests editing a product with PUT method"""
        product = Product.objects.create(sku='PROD-1', name='Razer Vyper', price=55.77, brand='Razer', created_at=make_aware(datetime.now()))
        payload = { 'sku': 'PROD-NEW', 'name': 'Logitech Mouse', 'price': 11.22, 'brand': 'Logitech'}
        with mock.patch('products.serializers.email_handler', return_value=True):   # Mock email handler to avoid spam email sending
            self.client.put(control_producturl(product.id), payload)
        product.refresh_from_db()
        self.assertEqual(product.sku, payload['sku'])
        self.assertEqual(product.name, payload['name'])
        self.assertEqual(float(product.price), payload['price'])
        self.assertEqual(product.brand, payload['brand'])

    def test_deleteprod_success(self):
        """Tests deleting a product"""
        product = Product.objects.create(sku='PROD-1', name='Razer Vyper', price=55.77, brand='Razer', created_at=make_aware(datetime.now()))
        self.client.delete(control_producturl(product.id))
        products = Product.objects.all()
        self.assertEqual(len(products), 0)
