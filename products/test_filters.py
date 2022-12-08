
import tempfile
from django.test import TestCase
from products.models import Category, Product
from django.urls import reverse


class TestProductsFilters(TestCase):
    """
    A Class to test the product filters
    """
    def setUp(self):
        """
        Setup regular user, superuser, test product, test category
        """
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
        Category.objects.all().delete()

    def test_ordered_product_list(self):
        """
        Tests weather the product list page loads ordered different ways
        """
        product = Product.objects.get(name='test_product')
        response = self.client.get(
            '/products/?price__iexact=&name__iexact=&' +
            'rating__iexact=&q=&ordering=price_asc'
            )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            '/products/?price__iexact=&name__iexact=&' +
            'rating__iexact=&q=&ordering=price_desc'
            )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            '/products/?price__iexact=&name__iexact=&' +
            'rating__iexact=&q=&ordering=name_desc'
            )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            '/products/?price__iexact=&name__iexact=&' +
            'rating__iexact=&q=&ordering=name_asc'
            )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            '/products/?price__iexact=&name__iexact=&' +
            'rating__iexact=&q=&ordering=rating_desc'
            )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            '/products/?price__iexact=&name__iexact=&' +
            'rating__iexact=&q=&ordering=rating_asc'
            )
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, template_name='base.html')
        self.assertTemplateUsed(
            response, template_name='products/product_list.html')

    def test_ordered_query_product_list(self):
        """
        This tests weather the search bar responds with a search query
        then orders it different ways
        """
        product = Product.objects.get(name='test_product')
        response = self.client.get(reverse('search_products'), {'q': 'test'})

        response = self.client.get(
            '/products/search/?q=test&ordering=price_asc'
            )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            '/products/search/?q=test&ordering=price_desc'
            )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            '/products/search/?q=test&ordering=name_desc'
            )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            '/products/search/?q=test&ordering=name_asc'
            )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            '/products/search/?q=test&ordering=rating_desc'
            )
        self.assertEqual(response.status_code, 200)

        response = self.client.get(
            '/products/search/?q=test&ordering=rating_asc'
            )
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, template_name='base.html')
        self.assertTemplateUsed(
            response, template_name='products/product_list.html')
