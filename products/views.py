"""
A module containing the views within products app.
"""
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponseRedirect)
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .product_filters import ProductFilter, ProductOrderFilter
from .models import Product, Category
from .forms import ProductModelForm, CategoryModelForm


class ListProducts(ListView):
    """
    A class to view all the products with filtering and sorting.
    """
    model = Product
    paginate_by = 12

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
    paginate_by = 12

    def __init__(self):
        self.no_search_result = True

    def get_queryset(self, **kwargs):
        search_results = ProductFilter(self.request.GET, self.queryset)
        queryset = search_results.qs.distinct()
        query = self.request.GET.get('q')
        if not query:
            messages.error(
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

    paginated_filtered_products = Paginator(filtered_products.qs, 12)

    page_number = request.GET.get('page')
    product_page_obj = paginated_filtered_products.get_page(page_number)

    context['cats'] = cats
    context['product_page_obj'] = product_page_obj

    return render(request, 'products/category.html', context)


class ProductCreate(UserPassesTestMixin, CreateView):
    """
    A class view to create products
    """
    template_name = 'products/create_product.html'
    form_class = ProductModelForm
    queryset = Product.objects.all()

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        messages.success(self.request, 'Product created successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"Error": "Something went wrong"})
        messages.error(
            self.request,
            "Sorry, something went wrong, please check the form again.")
        return self.render_to_response(context)

    def handle_no_permission(self):
        messages.error(
            self.request,
            "You do not have permission to view this page.")
        return redirect('/accounts/login')


class ProductUpdate(UserPassesTestMixin, UpdateView):
    """
    A class view to update products
    """
    template_name = 'products/create_product.html'
    form_class = ProductModelForm
    queryset = Product.objects.all()

    def test_func(self):
        return self.request.user.is_superuser

    def get_object(self, queryset=queryset):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=pk_)

    def form_valid(self, form):
        messages.success(self.request, "Product updated successfully.")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        If the form is invalid, render the invalid form.
        """
        messages.error(
            self.request,
            "Sorry there was an error, please check the form again.")
        return self.render_to_response(self.get_context_data(form=form))

    def handle_no_permission(self):
        messages.error(
            self.request,
            "You do not have permission to view this page.")
        return redirect('/accounts/login')


class ProductDelete(UserPassesTestMixin, DeleteView):
    """
    A class view to delete products
    """
    template_name = 'products/delete_object.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get_object(self, queryset=None):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=pk_)

    def get_success_url(self, **kwargs):
        messages.success(self.request, "Product deleted successfully.")
        success_url = reverse('all_products')
        return success_url

    def handle_no_permission(self):
        messages.error(
            self.request,
            "You do not have permission to view this page.")
        return redirect('/accounts/login')


class CategoryCreate(UserPassesTestMixin, CreateView):
    """
    A class view to create categories
    """
    model = Category
    form_class = CategoryModelForm
    template_name = 'products/create_category.html'

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        messages.success(self.request, 'Category created successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"Error": "Something went wrong"})
        messages.error(
            self.request,
            "Sorry, something went wrong, please check the form again.")
        return self.render_to_response(context)

    def handle_no_permission(self):
        messages.error(
            self.request,
            "You do not have permission to view this page.")
        return redirect('/accounts/login')

    success_url = '/products/categories/'


class CategoryUpdate(UserPassesTestMixin, UpdateView):
    """
    A class view to create categories
    """
    model = Category
    form_class = CategoryModelForm
    template_name = 'products/create_category.html'
    success_url = '/products/categories/'

    def test_func(self):
        return self.request.user.is_superuser

    raise_exception = False
    redirect_field_name = '/'

    def form_valid(self, form):
        messages.success(self.request, 'Category updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"Error": "Something went wrong"})
        messages.error(
            self.request,
            "Sorry, something went wrong, please check the form again.")
        return self.render_to_response(context)

    def handle_no_permission(self):
        messages.error(
            self.request,
            "You do not have permission to view this page.")
        return redirect('/accounts/login')


class CategoryDelete(UserPassesTestMixin, DeleteView):
    """
    A class view to delete categories
    """
    model = Category
    template_name = 'products/delete_object.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self, **kwargs):
        messages.success(self.request, "Category deleted successfully.")
        success_url = '/products/categories/'
        return success_url

    def handle_no_permission(self):
        messages.error(
            self.request,
            "You do not have permission to view this page.")
        return redirect('/accounts/login')
