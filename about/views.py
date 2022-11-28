"""
A module containing the views within the about app.
"""
from django.shortcuts import render
from .models import Faq


def about(request):
    """
    A view to display the about page
    """
    faqs = Faq.objects.all()
    return render(request, 'about/about.html', {'faqs': faqs, })
