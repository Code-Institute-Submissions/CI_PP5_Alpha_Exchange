"""
A module to filter the products different ways in the app.
"""
import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    """
    A class to apply different filters.
    """

    CHOICES = (
        ('price_asc', 'Price (Ascending)'),
        ('price_desc', 'Price (Descending)'),
        ('name_desc', 'Name (Descending)'),
        ('name_asc', 'Name (Ascending)'),
        ('rating_desc', 'Rating (Descending)'),
        ('rating_asc', 'Rating (Ascending)'),
    )

    ordering = django_filters.ChoiceFilter(
        label='Ordering',
        choices=CHOICES,
        method='filter_by_order'
        )

    class Meta:
        model = Product
        fields = {
            'price': ['iexact'],
            'name': ['iexact'],
            'rating': ['iexact'],
        }

    def filter_by_order(self, queryset, name, value):
        """
        A method to order items by value
        """
        if value == 'price_asc':
            expression = 'price'
        elif value == 'price_desc':
            expression = '-price'
        elif value == 'name_desc':
            expression = 'name'
        elif value == 'name_asc':
            expression = '-name'
        elif value == 'rating_asc':
            expression = 'rating'
        else:
            expression = '-rating'
        return queryset.order_by(expression)


class ProductOrderFilter(django_filters.FilterSet):
    """
    A class to filter the product model
    """

    CHOICES = (
        ('price_asc', 'Price (Ascending)'),
        ('price_desc', 'Price (Descending)'),
        ('name_desc', 'Name (Descending)'),
        ('name_asc', 'Name (Ascending)'),
        ('rating_desc', 'Rating (Descending)'),
        ('rating_asc', 'Rating (Ascending)'),
    )

    ordering = django_filters.ChoiceFilter(
        label='Ordering',
        choices=CHOICES,
        method='filter_by_order'
        )

    class Meta:
        model = Product
        fields = {}

    def filter_by_order(self, queryset, name, value):
        """
        A method to order items by value
        """
        if value == 'price_asc':
            expression = 'price'
        elif value == 'price_desc':
            expression = '-price'
        elif value == 'name_desc':
            expression = 'name'
        elif value == 'name_asc':
            expression = '-name'
        elif value == 'rating_asc':
            expression = 'rating'
        else:
            expression = '-rating'
        return queryset.order_by(expression)
