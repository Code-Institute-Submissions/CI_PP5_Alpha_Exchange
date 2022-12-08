"""
A module to test the Views for the contact app
"""
from django.test import TestCase
from django.contrib.messages import get_messages


class TestContactViews(TestCase):
    """
    A Class to test the Contact page view
    """
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
        response = self.client.post("/contact/", data={
            'name': 'Test Name',
            'email': 'test@email.com',
            'phone_number': '01234567890',
            'street_address1': '123 street',
            'street_address2': '',
            'town_or_city': 'somewhere',
            'county': '',
            'postcode': '123 ABC',
            'country': 'GB',
            'message': 'Test Message',
            })
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            "Thank you for your message we will be in touch with you soon.")
