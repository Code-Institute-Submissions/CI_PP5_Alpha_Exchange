"""
A module to test the contact app models
"""
from django.test import TestCase
from django.contrib.auth.models import User
from contact.models import Contact


class TestContactModel(TestCase):
    """
    A Class to test the Contact model
    """
    def setUp(self):
        User.objects.create_user(
            username='test',
            password='password',
            email='test@email.com'
        )
        Contact.objects.create(
            name='test',
            email='test@email.com',
            phone_number='01234567890',
            street_address1='123 street',
            street_address2='',
            town_or_city='somewhere',
            county='',
            postcode='123 ABC',
            country='GB',
            message='Test Message',
        )

    def tearDown(self):
        """
        Tear down the setup environment
        """
        Contact.objects.all().delete()

    def test_course_str_method(self):
        """
        This test tests the categories str method and verifies
        """
        contact = Contact.objects.get(name='test')
        self.assertEqual((contact.__str__()), contact.name)
