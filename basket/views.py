"""
A module containing the views within basket app.
"""
from django.shortcuts import render, redirect
from django.contrib import messages
from products.models import Product


def basket(request):
    """
    A view to display the current basket.
    """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    Add the given quantity of the item to the basket.
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request, f'Added {Product.name} to your basket!'
            )
    else:
        basket[item_id] = quantity
        messages.success(
            request, f'Added {Product.name} to your basket!'
            )

    request.session['basket'] = basket
    return redirect(redirect_url)
