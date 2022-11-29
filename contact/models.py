"""
A module containing models for the contact app.
"""
from django.db import models
from django_countries.fields import CountryField


class Contact(models.Model):
    """
    A model class to hold the contact information
    """

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)

    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80)
    town_or_city = models.CharField(max_length=40)
    county = models.CharField(max_length=80)
    postcode = models.CharField(max_length=20)
    country = CountryField(blank_label='Country *')

    message = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        """
        Returns the contact name as a string
        """
        return self.name
