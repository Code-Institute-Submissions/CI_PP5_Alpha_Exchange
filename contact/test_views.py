"""
A module to test the Views for the contact app
"""
from django.test import TestCase
from django.contrib.auth.models import User
from contact.models import Contact


class TestContactViews(TestCase):
    """
    A Class to test the Contact page view
    """
    def setUp(self):
        User.objects.create_user(
            username='test',
            password='password',
            email='test@email.com'
        )

    def test_contact_page(self):
        """
        Test the Contact page loading
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_contact_form(self):
        """
        Test the form filled out as a user and post
        """
        contact = User.objects.get(username='test')

        response = self.client.post("/contact/", data={
            'name': contact.username,
            'email': contact.email,
            'phone_number': '01234567890',
            'street_address1': '123 street',
            'street_address2': '',
            'town_or_city': 'somewhere',
            'county': '',
            'postcode': '123 ABC',
            'country': 'GB',
            'message': 'Test Message',
            })
