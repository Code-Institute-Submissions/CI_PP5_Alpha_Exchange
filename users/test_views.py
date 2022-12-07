"""
A Module to test the Basket views
"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from checkout.models import Order
from .models import UserAccount


class TestUserViews(TestCase):
    """
    A Class for testing the user views
    """
    def setUp(self):
        """
        Setup regular user, superuser, test product, test category
        """
        test_user = User.objects.create_user(
            username='test',
            password='password',
            email='test@email.com'
        )

    def tearDown(self):
        """
        Tear down the setup environment
        """
        User.objects.all().delete()

    def test_profile_page(self):
        """
        Test the profile page loading
        """
        test_user = self.client.login(username='test', password='password')
        response = self.client.get('/users/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_profile_form(self):
        """
        Test the profile page loading
        """
        self.client.login(username='test', password='password')
        response = self.client.post(f'/users/profile/', {
            'full_name': 'Mr Banks',
            'street_address1': '17 Cherry Tree Lane',
            'town_or_city': 'London',
            'country': 'GB',
            'email': 'test@email.com',
            'phone_number': '01234567890',
            'order_number': '01234567890'
        })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "Profile updated successfully")
