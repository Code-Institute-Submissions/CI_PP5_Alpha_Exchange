"""
A module for forms in the products app
"""
from django import forms
from .models import Product, Category, Review


class ProductModelForm(forms.ModelForm):
    """
    A form class for the Product model.
    """

    class Meta:
        model = Product
        # fields to include
        fields = [
            'category', 'sku', 'name', 'description',
            'price', 'rating', 'image', 'has_sizes',
            'recommended_use', 'featured',
            ]
        # wet custom widgets
        widgets = {
            'has_sizes': forms.CheckboxInput,
            'featured': forms.CheckboxInput,
            }

    def __init__(self, *args, **kwargs):
        """
        Override the default init method to add placeholders and classes,
        remove auto-generated labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # placeholders to overwrite
        placeholders = {
            'name': 'Product name',
            'sku': 'Product SKU',
            'description': 'Product description',
            'price': '£ - price',
            'rating': 'Product rating',
            'recommended_use': 'Recommended Use',
            'image': 'Image',
        }

        # set the placeholders, autofocus and style class
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            exempt_placeholders = [
                "has_sizes", "featured", "category"]
            if field not in exempt_placeholders:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class CategoryModelForm(forms.ModelForm):
    """
    A form class for the Product model.
    """
    class Meta:
        model = Category
        # use all fields
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # placeholders to overwrite
        placeholders = {
            'name': 'Category name',
            'friendly_name': 'Friendly Name',
            'image': 'Image'
        }

        # set the placeholders, autofocus and style class
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder


class ReviewForm(forms.ModelForm):
    """
    Form users to post their reviews.
    """
    class Meta:
        model = Review
        fields = ('title', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # placeholders to overwrite
        placeholders = {
            'title': 'Title',
            'message': 'Write your review...',
        }

        # set the placeholders, autofocus and style class
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
