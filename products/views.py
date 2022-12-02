"""
A module containing the views within the products app.
"""
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponseRedirect)
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, View)
from users.models import UserAccount
from .product_filters import ProductFilter, ProductOrderFilter
from .models import Product, Category, Review
from .forms import ProductModelForm, CategoryModelForm, ReviewForm


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
        # get search criteria
        query = self.request.GET.get('q')
        if not query:
            # send error message if nothing entered
            messages.error(
                self.request, 'You did not enter any search criteria'
                )
            return Product.objects.none()
        if query:
            # apply filters to all products
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


class ProductDetail(View):
    """
    Displays the product details page by product ID.
    """

    def get(self, request, product_id):
        """
        fetches the information on the product, reviews and likes.
        """
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=product_id)
        reviews = product.review.filter(approved=True).order_by("timestamp")
        number_of_reviews = reviews.count
        liked = False
        if request.user.is_authenticated:
            profile = get_object_or_404(UserAccount, user=request.user)
            if product.likes.filter(id=profile.id).exists():
                liked = True

        context = {
            'product': product,
            "reviews": reviews,
            "review_posted": False,
            "liked": liked,
            "review_form": ReviewForm(),
            'number_reviews': number_of_reviews,
        }

        return render(request, 'products/product_detail.html', context)

    def post(self, request, product_id):
        """
        Handles the review form post
        """
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=product_id)
        reviews = product.review.filter(approved=True).order_by("timestamp")
        liked = False
        if request.user.is_authenticated:
            profile = get_object_or_404(UserAccount, user=request.user)
            if product.likes.filter(id=profile.id).exists():
                liked = True

        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review_form.instance.author = profile
            review = review_form.save(commit=False)
            review.product = product
            review.save()
            messages.success(
                request, "Your review was has been posted successfully.")
        else:
            review_form = ReviewForm()
            messages.success(
                request,
                "Your review was not submitted, please check the form.")

        context = {
                "product": product,
                "reviews": reviews,
                "review_posted": True,
                "review_form": review_form,
                "liked": liked,
            }

        return render(
            request, 'products/product_detail.html', context)


class EditReview(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
     Allow users to edit their reviews.
    """
    queryset = Review.objects.all()
    template_name = 'products/edit_review.html'
    form_class = ReviewForm
    success_message = 'The review was successfully updated'


@login_required
def delete_review(request, review_id):
    """
    Delete user Reviews from the website
    """
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'The review was deleted successfully')
    return HttpResponseRedirect(reverse(
        'product_detail', args=[review.product.id]))


class ProductLike(View):
    """
    Adds or removes the like from a product
    """
    def post(self, request, product_id, *args, **kwargs):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=product_id)
        profile = get_object_or_404(UserAccount, user=request.user)
        if product.likes.filter(id=profile.id).exists():
            product.likes.remove(profile)
        else:
            product.likes.add(profile)

        return HttpResponseRedirect(
            reverse('product_detail', args=[product_id]))


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
    page_obj = paginated_filtered_products.get_page(page_number)

    context['cats'] = cats
    context['page_obj'] = page_obj

    return render(request, 'products/category.html', context)


class ProductCreate(UserPassesTestMixin, CreateView):
    """
    A class view to create products
    """
    template_name = 'products/create_product.html'
    form_class = ProductModelForm
    queryset = Product.objects.all()

    def test_func(self):
        # check if user is a superuser
        return self.request.user.is_superuser

    def form_valid(self, form):
        # if form was valid send success message
        messages.success(self.request, 'Product created successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        # if form was invalid send error message
        context.update({"Error": "Something went wrong"})
        messages.error(
            self.request,
            "Sorry, something went wrong, please check the form again.")
        return self.render_to_response(context)

    def handle_no_permission(self):
        # if user not allowed redirect and send message
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
        # check if user is a superuser
        return self.request.user.is_superuser

    def get_object(self, queryset=queryset):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=pk_)

    def form_valid(self, form):
        # if form was valid send success message and redirect to product
        messages.success(self.request, "Product updated successfully.")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        If the form is invalid, render the invalid form.
        """
        # if form was invalid send error message
        messages.error(
            self.request,
            "Sorry there was an error, please check the form again.")
        return self.render_to_response(self.get_context_data(form=form))

    def handle_no_permission(self):
        # if user not allowed redirect and send message
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
        # check if user is a superuser
        return self.request.user.is_superuser

    def get_object(self, queryset=None):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Product, pk=pk_)

    def get_success_url(self, **kwargs):
        # if form was valid send success message
        messages.success(self.request, "Product deleted successfully.")
        success_url = reverse('all_products')
        return success_url

    def handle_no_permission(self):
        # if user not allowed redirect and send message
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
        # check if user is a superuser
        return self.request.user.is_superuser

    def form_valid(self, form):
        # if form was valid send success message
        messages.success(self.request, 'Category created successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        # if form was invalid send error message
        context.update({"Error": "Something went wrong"})
        messages.error(
            self.request,
            "Sorry, something went wrong, please check the form again.")
        return self.render_to_response(context)

    def handle_no_permission(self):
        # if user not allowed redirect and send message
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
        # check if user is a superuser
        return self.request.user.is_superuser

    raise_exception = False
    redirect_field_name = '/'

    def form_valid(self, form):
        # if form was valid send success message and redirect to all categories
        messages.success(self.request, 'Category updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        # if form was invalid send error message
        context.update({"Error": "Something went wrong"})
        messages.error(
            self.request,
            "Sorry, something went wrong, please check the form again.")
        return self.render_to_response(context)

    def handle_no_permission(self):
        # if user not allowed redirect and send message
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
        # check if user is a superuser
        return self.request.user.is_superuser

    def get_success_url(self, **kwargs):
        # if form was valid send success message
        messages.success(self.request, "Category deleted successfully.")
        success_url = '/products/categories/'
        return success_url

    def handle_no_permission(self):
        # if user not allowed redirect and send message
        messages.error(
            self.request,
            "You do not have permission to view this page.")
        return redirect('/accounts/login')
