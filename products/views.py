"""
A module containing the views within products app.
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView
from .product_filters import ProductFilter, ProductOrderFilter
from .models import Product, Category


class ListProducts(ListView):
    """
    A class to view all the products with filtering and sorting.
    """
    model = Product
    paginate_by = 20

    def __init__(self):
        self.no_search_result = True

    def get_queryset(self, **kwargs):
        search_results = ProductFilter(self.request.GET, self.queryset)
        if search_results.qs:
            self.no_search_result = False
        # Returns the default queryset if an empty
        # queryset is returned by the django_filters
        return search_results.qs.distinct() or self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['filter'] = ProductFilter(
            self.request.GET, queryset=self.get_queryset()
            )
        return context


class SearchProduct(ListView):
    """
    A class to view the search results with filtering and sorting.
    """
    model = Product
    paginate_by = 20

    def __init__(self):
        self.no_search_result = True

    def get_queryset(self, **kwargs):
        search_results = ProductFilter(self.request.GET, self.queryset)
        queryset = search_results.qs.distinct()
        query = self.request.GET.get('q')
        if not query:
            messages.info(
                self.request, 'You did not enter any search criteria'
                )
            return Product.objects.none()
        if query:
            search_results = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(recommended_use__icontains=query)).distinct()
        if search_results:
            self.no_search_result = False
        # Returns the queryset returned by the django_filters
        return search_results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['filter'] = ProductOrderFilter(
            self.request.GET, queryset=Product.objects.all()
            )
        return context


def product_detail(request, product_id):
    """
    Displays the product details page by product ID.
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)


def categories(request):
    """
    Renders the categories page.
    """
    return render(request, 'products/categories.html')


def categories_view(request, cats):
    """
    Renders the products filtered by categories.
    """
    context = {}

    filtered_products = ProductOrderFilter(
        request.GET, queryset=Product.objects.filter(
            category__friendly_name__contains=cats))

    context['filter'] = filtered_products

    paginated_filtered_products = Paginator(filtered_products.qs, 4)

    page_number = request.GET.get('page')
    product_page_obj = paginated_filtered_products.get_page(page_number)

    context['cats'] = cats
    context['product_page_obj'] = product_page_obj

    return render(request, 'products/category.html', context)
