"""
A module containing the views within products app.
"""
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from .models import Product


def list_products(request, page=1):
    """
    Displays the list of products with filtering and search queries.
    """

    products = Product.objects.all()
    paginator = Paginator(products, 20)

    try:
        products = paginator.page(page)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'products/products.html', {'products': products})
