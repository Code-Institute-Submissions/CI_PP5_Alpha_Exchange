"""
A module containing the views within basket app.
"""
from django.shortcuts import render


def basket(request):
    """
    A view tp display the current basket.
    """
    return render(request, 'basket/basket.html')
