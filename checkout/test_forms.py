
"""
A Module for testing checkout forms
"""
from django.test import TestCase
from .forms import OrderForm


class TestCheckoutForms(TestCase):
    """
    A class for testing checkout forms
    """
    def test_add_order_form(self):
        """
        Test the OrderForm
        """
        form = OrderForm({
            'full_name': 'Mr Banks',
            'email': 'test@email.com',
            'phone_number': '01234567890',
            'street_address1': 'test address 1',
            'street_address2': 'test address 2',
            'town_or_city': 'test city',
            'postcode': 'postcode',
            'county': 'county',
            'country': 'GB',
            })
        self.assertTrue(form.is_valid())
