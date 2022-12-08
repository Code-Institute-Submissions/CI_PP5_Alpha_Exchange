"""
A Module to test the Products views
"""
import tempfile
from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.auth.models import User
from products.models import Category, Product
from products.views import ListProducts, SearchProduct
from products.forms import ProductModelForm
from django.shortcuts import get_object_or_404


class TestProductsClassView(TestCase):
    """
    A Class to test the products
    """
    def setUp(self):
        """
        Setup regular user, superuser, test product, test category
        """
        User.objects.create_user(
            username='test',
            password='password',
            email='test@email.com'
        )
        User.objects.create_superuser(
            username='test_super',
            password='password_super',
            email='test_super@email.com'
        )
        cat = Category.objects.create(
            name='test_category',
            friendly_name='test category',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name
        )
        product = Product.objects.create(
            name='test_product',
            category=cat,
            sku='sku999999',
            price='100',
            rating='3',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            has_sizes=1,
            recommended_use='test',
            featured=0,
            description='test'
        )

    def tearDown(self):
        """
        Tear down the setup environment
        """
        Product.objects.all().delete()
        User.objects.all().delete()
        Category.objects.all().delete()

    def test_product_detail(self):
        """
        Tests weather the products details page loads
        """
        product = Product.objects.get(name='test_product')
        response = self.client.get(
            f'/products/{product.id}', {'product': product})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_list(self):
        """
        Tests weather the product list page loads
        """
        product = Product.objects.get(name='test_product')

        response = self.client.get(reverse("all_products"))
        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            ListProducts.as_view().__name__,
            response.resolver_match.func.__name__)

        self.assertTemplateUsed(response, template_name='base.html')
        self.assertTemplateUsed(
            response, template_name='products/product_list.html')

    def test_no_search__query(self):
        """
        This tests weather the search bar responds
        with an error for no search query
        """
        response = self.client.get(reverse('search_products'), {'q': ''})
        self.assertContains(
            response,
            'You did not enter any search criteria'
            )

    def test_with_search_query(self):
        """
        This tests weather the search bar responds with a search query
        """
        product = Product.objects.get(name='test_product')
        response = self.client.get(reverse('search_products'), {'q': 'test'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            SearchProduct.as_view().__name__,
            response.resolver_match.func.__name__)

        self.assertTemplateUsed(response, template_name='base.html')
        self.assertTemplateUsed(
            response, template_name='products/product_list.html')

    def test_categories_page(self):
        """
        Tests weather the categories page loads
        """
        response = self.client.get('/products/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/categories.html')

    def test_category(self):
        """
        Tests weather the category page loads
        """
        category = Category.objects.get(name='test_category')
        response = self.client.get(f'/products/categories_list/'
                                   f'{category.friendly_name}',
                                   {'category': category})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/category.html')

    def test_product_create_admin(self):
        """
        Tests loading create product page as admin
        """
        self.client.login(username='test_super', password='password_super')
        response = self.client.get('/products/create_product/')
        self.assertTemplateUsed(response, 'products/create_product.html')

    def test_product_create_no_admin(self):
        """
        Tests loading create product page as non admin
        """
        self.client.login(username='test', password='password')
        response = self.client.get('/products/create_product/')
        self.assertRedirects(
            response, '/accounts/login', target_status_code=301)

    def test_product_update_no_admin(self):
        """
        Tests loading update product page as non admin
        """
        product = Product.objects.get(name='test_product')
        self.client.login(username='test', password='password')
        response = self.client.get(f'/products/update/{product.id}/')
        self.assertRedirects(
            response, '/accounts/login', target_status_code=301)

    def test_product_update_admin(self):
        """
        Tests loading update product page as admin
        """
        self.client.login(username='test_super', password='password_super')
        product = Product.objects.get(name='test_product')
        category = Category.objects.get(name='test_category')
        response = self.client.get(f'/products/update/{product.id}/')
        self.assertTemplateUsed(response, template_name='base.html')
        self.assertTemplateUsed(
            response, template_name='products/create_product.html')

    def test_product_delete_no_admin(self):
        """
        Tests loading delete product page as non admin
        """
        product = Product.objects.get(name='test_product')
        self.client.login(username='test', password='password')
        response = self.client.get(f'/products/delete/{product.id}/')
        self.assertRedirects(
            response, '/accounts/login', target_status_code=301)

    def test_product_delete_admin(self):
        """
        Tests loading delete product page as admin
        """
        self.client.login(username='test_super', password='password_super')
        product = Product.objects.get(name='test_product')
        response = self.client.get(f'/products/delete/{product.id}/')
        self.assertTemplateUsed(response, template_name='base.html')
        self.assertTemplateUsed(
            response, template_name='products/delete_object.html')

    def test_category_create_admin(self):
        """
        Tests loading create category page as admin
        """
        self.client.login(username='test_super', password='password_super')
        response = self.client.get('/products/create_category/')
        self.assertTemplateUsed(response, 'products/create_category.html')

    def test_category_create_no_admin(self):
        """
        Tests loading create category page as non admin
        """
        self.client.login(username='test', password='password')
        response = self.client.get('/products/create_category/')
        self.assertRedirects(
            response, '/accounts/login', target_status_code=301)

    def test_category_update_no_admin(self):
        """
        Tests loading update category page as non admin
        """
        category = Category.objects.get(name='test_category')
        self.client.login(username='test', password='password')
        response = self.client.get(f'/products/{category.id}/update_category/')
        self.assertRedirects(
            response, '/accounts/login', target_status_code=301)

    def test_category_update_admin(self):
        """
        Tests loading update category page as admin
        """
        self.client.login(username='test_super', password='password_super')
        category = Category.objects.get(name='test_category')
        response = self.client.get(f'/products/{category.id}/update_category/')
        self.assertTemplateUsed(response, template_name='base.html')
        self.assertTemplateUsed(
            response, template_name='products/create_category.html')

    def test_category_delete_no_admin(self):
        """
        Tests loading delete category page as non admin
        """
        category = Category.objects.get(name='test_category')
        self.client.login(username='test', password='password')
        response = self.client.get(f'/products/{category.id}/delete_category/')
        self.assertRedirects(
            response, '/accounts/login', target_status_code=301)

    def test_category_delete_admin(self):
        """
        Tests loading delete category page as admin
        """
        self.client.login(username='test_super', password='password_super')
        category = Category.objects.get(name='test_category')
        response = self.client.get(f'/products/{category.id}/delete_category/')
        self.assertTemplateUsed(response, template_name='base.html')
        self.assertTemplateUsed(
            response, template_name='products/delete_object.html')

    def test_load_page_two(self):
        """
        Tests if pages two of all products page will load
        """
        cat = Category.objects.get(name='test_category')
        product1 = Product.objects.create(name=f'test_product1',
                                          category=cat, description='test',
                                          price='100', recommended_use='test')
        product2 = Product.objects.create(name=f'test_product2',
                                          category=cat, description='test',
                                          price='100', recommended_use='test')
        product3 = Product.objects.create(name=f'test_product3',
                                          category=cat, description='test',
                                          price='100', recommended_use='test')
        product4 = Product.objects.create(name=f'test_product4',
                                          category=cat, description='test',
                                          price='100', recommended_use='test')
        product5 = Product.objects.create(name=f'test_product5',
                                          category=cat, description='test',
                                          price='100', recommended_use='test')
        product6 = Product.objects.create(name=f'test_product6',
                                          category=cat, description='test',
                                          price='100', recommended_use='test')
        product7 = Product.objects.create(name=f'test_product7',
                                          category=cat, description='test',
                                          price='100', recommended_use='test')
        product8 = Product.objects.create(name=f'test_product8',
                                          category=cat, description='test',
                                          price='100', recommended_use='test')
        product9 = Product.objects.create(name=f'test_product9',
                                          category=cat, description='test',
                                          price='100', recommended_use='test')
        product10 = Product.objects.create(name=f'test_product10',
                                           category=cat, description='test',
                                           price='100', recommended_use='test')
        product11 = Product.objects.create(name=f'test_product11',
                                           category=cat, description='test',
                                           price='100', recommended_use='test')
        product12 = Product.objects.create(name=f'test_product12',
                                           category=cat, description='test',
                                           price='100', recommended_use='test')
        product13 = Product.objects.create(name=f'test_product13',
                                           category=cat, description='test',
                                           price='100', recommended_use='test')
        product14 = Product.objects.create(name=f'test_product14',
                                           category=cat, description='test',
                                           price='100', recommended_use='test')
        product15 = Product.objects.create(name=f'test_product15',
                                           category=cat, description='test',
                                           price='100', recommended_use='test')

        response = self.client.get(reverse('all_products'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/products/?page=2')
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, template_name='base.html')
        self.assertTemplateUsed(
            response, template_name='products/product_list.html')
