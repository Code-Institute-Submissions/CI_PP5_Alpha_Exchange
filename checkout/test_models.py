"""
A Module for testing the checkout models
"""
from django.test import TestCase
from .models import Order


class TestCheckoutModels(TestCase):
    """
    A class for testing checkout models
    """
    def setUp(self):
        """
        Create a test product and order
        """
        Order.objects.create(
            full_name='someone',
            email='test@email.com',
            phone_number='01234567890',
            street_address1='123',
            street_address2='street',
            town_or_city='somewhere',
            postcode='somewhen',
            county='somehow',
            country='GB',
        )

    def tearDown(self):
        """
        Delete test products and orders
        """
        Order.objects.all().delete()

    def test_order_str_method(self):
        """
        This test tests the order number string
        """
        order = Order.objects.get(full_name='someone')
        self.assertEqual(str(order), order.order_number)
