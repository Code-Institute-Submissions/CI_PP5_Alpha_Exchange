"""
A module containing the views within basket app.
"""
from django.shortcuts import render, redirect, get_object_or_404
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
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['item_sizes'].keys():
                basket[item_id]['item_sizes'][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} quantity to {basket[item_id]["item_sizes"][size]}')
            else:
                basket[item_id]['item_sizes'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} to your basket')
        else:
            basket[item_id] = {'item_sizes': {size: quantity}}
            messages.success(
                request,
                f'Added size {size.upper()} {product.name} to your basket')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(
                request, f'Updated {Product.name} in your basket!'
                )
        else:
            basket[item_id] = quantity
            messages.success(
                request, f'Added {Product.name} to your basket!'
                )

    request.session['basket'] = basket
    return redirect(redirect_url)
