from datetime import datetime

import pytz
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.timezone import make_aware
from rest_framework.test import APIClient
from rest_framework import status
from user.serializers import UserSerializerAdmin

TOKEN_URL = reverse('user:authtoken')
USER_LISTURL = reverse('user:user_list')
USER_CREATEURL = reverse('user:user_create')


def create_user(**params):
    """User create function"""
    return get_user_model().objects.create_user(**params)


def manage_userurl(pk=1):
    """Returns user unique url"""
    return reverse('user:user_manage', args=[pk])


class UserAnonTests(TestCase):
    """Tests for user api for anonymous users"""

    def setUp(self):
        self.client = APIClient()

    def test_userview_noauth_fail(self):
        """Test that authentication is required for users"""
        response = self.client.get(manage_userurl())
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_viewusers_noauth_fail(self):
        """Tests that unauthorized users cannot view users"""
        create_user(username='test1', email='test1@test.com', password='test33')
        create_user(username='test2', email='test2@test.com', password='test44')
        result = self.client.get(USER_LISTURL)
        self.assertEqual(result.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_createuser_noauth_fail(self):
        """Tests that unauthorized users cannot create users"""
        payload = {'username': 'test1', 'password': 'test33'}
        result = self.client.post(USER_CREATEURL, payload)
        self.assertEqual(result.status_code, status.HTTP_401_UNAUTHORIZED)


class UserAdminTests(TestCase):
    """Tests for user api for admin users"""

    def setUp(self):
        self.user = create_user(username='admin', email='admintest@admin.com', password='password123', is_staff=True, date_joined=make_aware(datetime.now()))
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_authtoken_invalidcred_fail(self):
        """Tests for invalid credentials"""
        payload = {'username': 'admin', 'password': 'otherpass'}
        response = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_authtoken_invaliduser_fail(self):
        """Tests for invalid user"""
        payload = {'username': 'otheruser', 'password': 'password123'}
        response = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_authtoken_success(self):
        """ Tests that token is created for admin users"""
        payload = {'username': 'admin', 'password': 'password123'}  # same as setUp
        result = self.client.post(TOKEN_URL, payload)
        self.assertIn('token', result.data)
        self.assertEqual(result.status_code, status.HTTP_200_OK)

    def test_authtoken_missingfield_fail(self):
        """Tests for missing fields"""
        payload = {'username': 'admin', 'password': ''}
        response = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_userviews_success(self):
        """Tests Viewset for admin users"""
        create_user(username='admin1', email='adminemail1@admin.com', password='password123')
        create_user(username='admin2', email='adminemail2@admin.com', password='password123')
        result = self.client.get(USER_LISTURL)
        users = get_user_model().objects.all()
        serializer = UserSerializerAdmin(users, many=True)
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data, serializer.data)

    def test_createuser_success(self):
        """Tests that admin users can create users"""
        data = { 'username': 'testuser', 'email': 'new_user@test.com', 'password': 'password123'}
        result = self.client.post(USER_CREATEURL, data)
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**result.data)
        self.assertTrue(user.check_password(data['password']))
        self.assertNotIn('password', result.data)

    def test_createuser_duplicate_fail(self):
        """Tests that duplicate users cannot be created"""
        payload = {'username': 'test1', 'password': 'password123', }
        result = self.client.post(USER_CREATEURL, payload)
        self.assertEqual(result.status_code, status.HTTP_400_BAD_REQUEST)

    def test_useradminviewset_success(self):
        """Test retrieving profile for existent user"""
        response = self.client.get(manage_userurl(self.user.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'is_active': self.user.is_active,
            'is_staff': self.user.is_staff,
        })

    def test_userupdate_patch_success(self):
        """Tests updating user with patch"""
        payload = {'username': 'nueusername', 'password': 'newpassword'}
        response = self.client.patch(manage_userurl(self.user.id), payload)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, payload['username'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_userupdate_put_success(self):
        """Tests updating user with put"""
        payload = {'username': 'newusername', 'email': 'new_user@admin.com', 'password': 'newpassword'}
        response = self.client.put(manage_userurl(self.user.id), payload)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, payload['username'])
        self.assertEqual(self.user.email, payload['email'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
