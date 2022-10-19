"""
A module containing the views within products app.
"""
from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """
    Displays the product details page by product ID.
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)
