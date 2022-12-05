"""
A module to test the about app models
"""
from django.test import TestCase
from django.contrib.auth.models import User
from about.models import Faq
import django
import os


class TestAboutModel(TestCase):
    """
    A Class to test the Faq model
    """
    def setUp(self):
        User.objects.create_user(
            username='test',
            password='password',
            email='test@email.com'
        )
        Faq.objects.create(
            title='test_faq',
            friendly_title='Test Faq',
            question='Test question',
            answer='Test answer'
        )

    def tearDown(self):
        """
        Tear down the setup environment
        """
        Faq.objects.all().delete()

    def test_course_str_method(self):
        """
        This test tests the categories str method and verifies
        """
        faq = Faq.objects.get(title='test_faq')
        self.assertEqual((faq.__str__()), faq.title)
