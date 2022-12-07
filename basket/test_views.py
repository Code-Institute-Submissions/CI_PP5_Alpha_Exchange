"""
A Module to test the Basket views
"""
from django.test import TestCase
import tempfile
from products.models import Product, Category
from django.contrib.messages import get_messages


class TestBasketViews(TestCase):
    """
    A Class for testing the basket views
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
        product = Product.objects.create(
            name='test_product2',
            category=cat,
            sku='sku999998',
            price='100',
            rating='3',
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            has_sizes=0,
            recommended_use='test',
            featured=0,
            description='test'
        )

    def tearDown(self):
        """
        Tear down the setup environment
        """
        Product.objects.all().delete()

    def test_basket_page(self):
        """
        Tests an empty basket page loading
        """
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')

    def test_add_basket_no_size(self):
        """
        Tests adding a product without a size,
        then adds a second to update the quantity
        """
        product = Product.objects.get(name='test_product2')
        response = self.client.post(f'/basket/add/{product.id}/',
                                    {"quantity": 1, "redirect_url": "basket"})
        basket = self.client.session['basket']
        self.assertEqual(list(basket.keys())[0], f'{product.id}')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), f'Added {product.name} to your basket!')

        response = self.client.post(f'/basket/add/{product.id}/',
                                    {"quantity": 1, "redirect_url": "basket"})
        basket = self.client.session['basket']
        self.assertEqual(list(basket.keys())[0], f'{product.id}')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]), f'Updated {product.name} in your basket!')

    def test_add_basket_with_size(self):
        """
        Tests adding a product with a size
        then adds a second to update the quantity
        then adds a third with a different size
        """
        product = Product.objects.get(name='test_product')
        response = self.client.post(f'/basket/add/{product.id}/',
                                    {"quantity": 1,
                                     "product_size": "m",
                                     "redirect_url": "basket"})
        basket = self.client.session['basket']
        self.assertEqual(list(basket.keys())[0], f'{product.id}')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), f'Added size M {product.name}, ' +
            'with quantity 1 to your basket.')

        response = self.client.post(f'/basket/add/{product.id}/',
                                    {"quantity": 1,
                                     "product_size": "m",
                                     "redirect_url": "basket"})
        basket = self.client.session['basket']
        self.assertEqual(list(basket.keys())[0], f'{product.id}')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]), f'Updated size M {product.name} quantity to 2')

        response = self.client.post(f'/basket/add/{product.id}/',
                                    {"quantity": 1,
                                     "product_size": "l",
                                     "redirect_url": "basket"})
        basket = self.client.session['basket']
        self.assertEqual(list(basket.keys())[0], f'{product.id}')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[2]), f'Added size L {product.name} to your basket')

    def test_adjust_basket_qty_no_size(self):
        """
        Tests adjusting the quantity of an item in the basket
        from 2 down to 1 then again to 0 without a size
        """
        product = Product.objects.get(name='test_product2')
        response = self.client.post(f'/basket/add/{product.id}/',
                                    {"quantity": 2, "redirect_url": "basket"})
        basket = self.client.session['basket']
        self.assertEqual(list(basket.keys())[0], f'{product.id}')

        response = self.client.post(f'/basket/adjust/{product.id}/', {
            'quantity': 1, "redirect_url": "basket",
        })
        self.assertRedirects(response, '/basket/')
        basket = self.client.session['basket']
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]), f'Updated {product.name} in your basket!')

        response = self.client.post(f'/basket/adjust/{product.id}/', {
            'quantity': 0, "redirect_url": "basket",
        })
        self.assertRedirects(response, '/basket/')
        basket = self.client.session['basket']
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), f'Removed {product.name} from your basket!')

    def test_adjust_basket_qty_with_size(self):
        """
        Tests adjusting the quantity of an item in the basket
        from 2 down to 1 then again to 0 with a size
        """
        product = Product.objects.get(name='test_product')
        response = self.client.post(f'/basket/add/{product.id}/',
                                    {"quantity": 2,
                                     "product_size": "m",
                                     "redirect_url": "basket"})
        basket = self.client.session['basket']
        self.assertEqual(list(basket.keys())[0], f'{product.id}')

        response = self.client.post(f'/basket/adjust/{product.id}/',
                                    {"quantity": 1,
                                     "product_size": "m",
                                     "redirect_url": "basket"})
        self.assertRedirects(response, '/basket/')
        basket = self.client.session['basket']
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]), f'Updated size M {product.name} quantity to 1')

        response = self.client.post(f'/basket/adjust/{product.id}/',
                                    {"quantity": 0,
                                     "product_size": "m",
                                     "redirect_url": "basket"})
        self.assertRedirects(response, '/basket/')
        basket = self.client.session['basket']
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), f'Removed {product.name} from your basket!')

    def test_remove_item_with_size(self):
        """
        Tests removing an item in the basket with size
        """
        product = Product.objects.get(name='test_product')
        response = self.client.post(f'/basket/add/{product.id}/',
                                    {"quantity": 1,
                                     "product_size": "m",
                                     "redirect_url": "basket"})
        response = self.client.post(f'/basket/add/{product.id}/',
                                    {"quantity": 1,
                                     "product_size": "l",
                                     "redirect_url": "basket"})
        basket = self.client.session['basket']
        self.assertEqual(list(basket.keys())[0], f'{product.id}')

        response = self.client.post(f'/basket/remove/{product.id}/',
                                    {"quantity": 1,
                                     "product_size": "l",
                                     "redirect_url": "basket"})
        basket = self.client.session['basket']
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[2]), f'Removed size L {product.name} from your bag')

        response = self.client.post(f'/basket/remove/{product.id}/',
                                    {"quantity": 1,
                                     "product_size": "m",
                                     "redirect_url": "basket"})
        basket = self.client.session['basket']
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[2]), f'Removed size L {product.name} from your bag')

    def test_remove_item_no_size(self):
        """
        Tests removing an item in the basket without size
        """
        product = Product.objects.get(name='test_product2')
        response = self.client.post(f'/basket/add/{product.id}/',
                                    {"quantity": 1,
                                     "redirect_url": "basket"})
        basket = self.client.session['basket']
        self.assertEqual(list(basket.keys())[0], f'{product.id}')

        response = self.client.post(f'/basket/remove/{product.id}/')
        basket = self.client.session['basket']
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[1]), f'{product.name} was removed from your basket!')

    def test_remove_deleted_item(self):
        """
        Tests removing item removed from the store
        """
        product = Product.objects.get(name='test_product2')
        response = self.client.post(f'/basket/remove/{product.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            f"'{product.id}' was not removed from the " +
            "basket correctly, please try again!")
