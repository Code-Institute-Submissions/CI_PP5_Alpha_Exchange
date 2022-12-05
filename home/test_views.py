"""
A module to test the Views for the home app
"""
from django.test import TestCase


class TestHomeViews(TestCase):
    """
    A Class to test the Home page view
    """
    def test_home_page(self):
        """
        Test the Home page loading
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
