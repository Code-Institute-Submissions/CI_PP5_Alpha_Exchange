"""
A module for forms in the products app
"""
from django import forms
from .models import Product, Category


class ProductModelForm(forms.ModelForm):
    """
    A form class for the Product model.
    """

    class Meta:
        model = Product
        fields = [
            'category', 'sku', 'name', 'description',
            'price', 'rating', 'image', 'has_sizes',
            'recommended_use', 'featured',
            ]
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
        placeholders = {
            'name': 'Product name',
            'sku': 'Product SKU',
            'description': 'Product description',
            'price': '£ - price',
            'rating': 'Product rating',
            'recommended_use': 'Recommended Use',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            exempt_placeholders = [
                "has_sizes", "featured", "category", "image"]
            if field not in exempt_placeholders:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
