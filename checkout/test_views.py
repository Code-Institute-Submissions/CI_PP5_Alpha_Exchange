"""
A Module for testing the checkout views
"""
from django.test import TestCase
from django.contrib.messages import get_messages
from django.urls import reverse
from users.models import UserAccount
from products.models import Category, Product
import tempfile


class TestCheckoutViews(TestCase):
    """
    A Class to test the checkout views
    """
    def test_empty_basket(self):
        """
        Test an empty basket at checkout
        """
        response = self.client.get('/checkout/')
        self.assertRedirects(
            response, reverse('all_products'))
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "There's nothing in your basket at the moment")
