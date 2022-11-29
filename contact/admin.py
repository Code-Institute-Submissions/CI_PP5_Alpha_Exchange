"""
A Module to hold the admin configuration.
"""
from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """
    Admin Class for Contact Model
    """
    list_display = ('name', 'email', 'message', 'phone_number')

    list_filter = ('name', 'email')

    search_fields = ('name', 'email')


admin.site.register(Contact, ContactAdmin)
