"""
A Module for testing the checkout models
"""
from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Category, Product
import tempfile


class TestCheckoutModels(TestCase):
    """
    A class for testing checkout models
    """
    def setUp(self):
        """
        Create a test product and order
        """
        cat = Category.objects.create(
            name='test_category',
            friendly_name='test category',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        test_product = Product.objects.create(
            name='test_product',
            category=cat,
            sku='sku999999',
            price='16.00',
            rating='3',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            has_sizes=1,
            recommended_use='test',
            featured=0,
            description='test'
        )
        test_product2 = Product.objects.create(
            name='test_product2',
            category=cat,
            sku='sku999999',
            price='60.00',
            rating='3',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            has_sizes=1,
            recommended_use='test',
            featured=0,
            description='test'
        )
        test_order = Order.objects.create(
            full_name='someone',
            email='test@email.com',
            phone_number='01234567890',
            street_address1='123',
            street_address2='street',
            town_or_city='somewhere',
            postcode='somewhen',
            county='somehow',
            country='GB',
            order_total='0.00'
        )
        OrderLineItem.objects.create(
            order=test_order,
            product=test_product,
            product_size='m',
            quantity=1,
            lineitem_total=test_product.price
        )
        OrderLineItem.objects.create(
            order=test_order,
            product=test_product2,
            product_size='l',
            quantity=1,
            lineitem_total=test_product.price
        )

    def tearDown(self):
        """
        Delete test products and orders
        """
        Order.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()

    def test_order_str_method(self):
        """
        This test tests the order number string
        """
        order = Order.objects.get(full_name='someone')
        self.assertEqual(str(order), order.order_number)

    def test_order_update_method_below_threshold(self):
        """
        Test the update order grand total method
        below delivery threshold
        """
        order = Order.objects.get(full_name='someone')
        self.assertEqual(str(order), order.order_number)
        orderlineitem = OrderLineItem.objects.get(product_size='m')
        response = self.client.get('/checkout/')
        self.assertEqual(
            order.grand_total, order.order_total)

    def test_order_update_method_above_threshold(self):
        """
        Test the update order grand total method
        above delivery threshold
        """
        order = Order.objects.get(full_name='someone')
        self.assertEqual(str(order), order.order_number)
        orderlineitem = OrderLineItem.objects.get(product_size='l')
        self.assertEqual(
            order.grand_total, order.order_total)
