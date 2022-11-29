"""
A module for the contact us forms
"""
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    A class to create the contact form
    """
    class Meta:
        model = Contact
        fields = '__all__'
