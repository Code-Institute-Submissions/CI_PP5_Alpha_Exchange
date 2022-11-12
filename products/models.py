"""
A module containing the models within products app.
"""
from django.db import models


class Category(models.Model):
    """
    A class for the category model.
    """
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        Returns the category name as a string.
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the category friendly_name as a string.
        """
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, default=3)
    image = models.ImageField(null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    recommended_use = models.CharField(max_length=254)
    featured = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        ordering = ['-featured']

    def __str__(self):
        return self.name
