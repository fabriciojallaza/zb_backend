from django.db import IntegrityError
from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminAppTests(TestCase):
    def setUp(self):
        """Setup for admin tests"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_user(
            username='admin_user',
            email='admin_user@admin.com',
            password='admin_user',
            is_staff=True,
            is_superuser=True,  # Admin user
        )
        self.client.force_login(self.admin_user)  # Login as admin user
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='test@test.com',
            password='pasword123',
        )

    def test_listusers_success(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.email)

    def test_editusers_viewloads_success(self):
        """Test that the user edit page loads"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # 200 = OK

    def test_createusers_viewloads_success(self):
        """Test that the user create page loads"""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # 200 = OK


class UsersModelTests(TestCase):

    def test_createuser_success(self):
        """Test for creating a new user"""
        username = 'test_user'
        email = 'test_user@test.com'
        password = 'password123'
        user = get_user_model().objects.create_user(username, email=email, password=password)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_createadminuser_success(self):
        """Test for creating a new admin user"""
        username = 'test_admin'
        email = 'test_admin@admin.com'
        password = 'password123'
        user = get_user_model().objects.create_user(username=username, email=email, password=password,
            is_staff=True,
            is_superuser=True,
        )
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_createuser_nousername_fail(self):
        """Test for creating a new user without an email"""
        with self.assertRaises(IntegrityError):
            get_user_model().objects.create_user(None, 'password123')
