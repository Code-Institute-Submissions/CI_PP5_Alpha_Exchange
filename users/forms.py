"""
A module containing the forms for the users app.
"""
from django import forms
from .models import UserAccount


class UserAccountForm(forms.ModelForm):
    """
    A class placing an order on the website.
    """
    class Meta:
        model = UserAccount
        # only exclude user field
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Override the default init method to add placeholders and classes,
        remove auto-generated labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        # placeholders to overwrite
        placeholders = {
            'default_full_name': 'Full Name',
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County, State or Locality',
            'default_postcode': 'Postal Code',
        }

        # set the placeholders, autofocus and style class
        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if not self.fields[field].required:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'rounded profile-form'
