"""
A module containing the models within products app.
"""
from django.db import models
from users.models import UserAccount
from django.urls import reverse


class Category(models.Model):
    """
    A class for the category model.
    """
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        Returns the category name as a string.
        """
        return self.name

    def get_friendly_name(self):
        """
        Returns the category friendly_name as a string.
        """
        return self.friendly_name


class Product(models.Model):
    """
    A class for the products available
    """
    name = models.CharField(max_length=254)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, default=3)
    image = models.ImageField(null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    recommended_use = models.CharField(max_length=254)
    featured = models.BooleanField(default=False, null=True, blank=True)
    likes = models.ManyToManyField(
        UserAccount, related_name='product_likes', blank=True)

    class Meta:
        ordering = ['-featured']

    def __str__(self):
        # return the name
        return self.name

    def number_of_likes(self):
        # Returns the number of likes
        return self.likes.count()

    def save(self, *args, **kwargs):
        """
        save the Product and if it doesn't have a sku set
        the next available unused number
        """
        if self.sku not in kwargs:
            self.sku = f'sku100{Product.objects.count() + 1}'
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """
        A method to return the absolute url
        """
        return reverse('product_detail', args=[str(self.pk)])


class Review(models.Model):
    """
    A class for people to leave a review
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="review")
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=500, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"Comment {self.title} by {self.author}"

    def get_absolute_url(self):
        """Sets the slug"""
        return reverse('product_detail', args=[self.product.slug])
