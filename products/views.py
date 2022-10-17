"""
A module containing the views within products app.
"""
from django.shortcuts import render
from .models import Product


def list_products(request):
    """
    Displays the list of products with filtering and search queries.
    """

    products = Product.objects.all()

    context = {
        'products': products,
        }

    return render(request, 'products/products.html', context)
