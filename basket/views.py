"""
A module containing the views within basket app.
"""
from django.shortcuts import (
    render, redirect, get_object_or_404, reverse, HttpResponse)
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
                    f'Updated size {size.upper()} {product.name} quantity ' +
                    f'to {basket[item_id]["item_sizes"][size]}')
            else:
                basket[item_id]['item_sizes'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} to your basket')
        else:
            basket[item_id] = {'item_sizes': {size: quantity}}
            messages.success(
                request,
                f'Added size {size.upper()} {product.name}, with quantity' +
                f' {basket[item_id]["item_sizes"][size]} to your basket.')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(
                request, f'Updated {product.name} in your basket!'
                )
        else:
            basket[item_id] = quantity
            messages.success(
                request, f'Added {product.name} to your basket!'
                )

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Change the quantity of an item in the basket.
    """
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if quantity > 0:
            basket[item_id]['item_sizes'][size] = quantity
        else:
            del basket[item_id]['item_sizes'][size]
            if not basket[item_id]['item_sizes']:
                basket.pop(item_id)
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('basket'))


def remove_basket(request, item_id):
    """
    Remove an item from the basket.
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        basket = request.session.get('basket', {})

        if size:
            del basket[item_id]['item_sizes'][size]
            if not basket[item_id]['item_sizes']:
                basket.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag')
        else:
            basket.pop(item_id)
            messages.success(
                request, f'{product.name} was removed from your basket!'
                )

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request,
            f'{e} was not removed from the basket correctly, please try again!'
            )
        return HttpResponse(status=500)
