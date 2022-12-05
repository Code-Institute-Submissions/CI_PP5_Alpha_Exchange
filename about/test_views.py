"""
A module to test the Views for the about app
"""
from django.test import TestCase


class TestAboutViews(TestCase):
    """
    A Class to test the About page view
    """
    def test_about_page(self):
        """
        Test the About page loading
        """
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')
