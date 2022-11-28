"""
A module containing the views within the basket app.
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

    # check for sizes
    if size:
        # check if item is in the basket
        if item_id in list(basket.keys()):
            # check if item of the same size is in the basket
            if size in basket[item_id]['item_sizes'].keys():
                # update quantity in basket
                basket[item_id]['item_sizes'][size] += quantity
                messages.info(
                    request,
                    f'Updated size {size.upper()} {product.name} quantity ' +
                    f'to {basket[item_id]["item_sizes"][size]}')
            else:
                # add new item to basket
                basket[item_id]['item_sizes'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} to your basket')
        else:
            # add new item to basket
            basket[item_id] = {'item_sizes': {size: quantity}}
            messages.success(
                request,
                f'Added size {size.upper()} {product.name}, with quantity' +
                f' {basket[item_id]["item_sizes"][size]} to your basket.')
    # items with no sizes
    else:
        # check if item is in the basket
        if item_id in list(basket.keys()):
            # update quantity in basket
            basket[item_id] += quantity
            messages.info(
                request, f'Updated {product.name} in your basket!'
                )
        else:
            # add new item to basket
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
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    # check for sizes
    if size:
        # check quantity more than 0
        if quantity > 0:
            # update quantity in basket
            basket[item_id]['item_sizes'][size] = quantity
            messages.info(
                    request,
                    f'Updated size {size.upper()} {product.name} quantity ' +
                    f'to {basket[item_id]["item_sizes"][size]}')
        else:
            # remove item from basket
            del basket[item_id]['item_sizes'][size]
            if not basket[item_id]['item_sizes']:
                basket.pop(item_id)
            messages.warning(
                request, f'Removed {product.name} from your basket!'
                )
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.info(
                request, f'Updated {product.name} in your basket!'
                )
        else:
            # remove item from basket
            basket.pop(item_id)
            messages.warning(
                request, f'Removed {product.name} from your basket!'
                )

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

        # check for sizes
        if size:
            # remove item of only this size
            del basket[item_id]['item_sizes'][size]
            if not basket[item_id]['item_sizes']:
                basket.pop(item_id)
            messages.warning(
                request,
                f'Removed size {size.upper()} {product.name} from your bag')
        else:
            # remove item
            basket.pop(item_id)
            messages.warning(
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
