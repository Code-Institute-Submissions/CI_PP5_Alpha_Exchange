"""
A Module for handling the shopping basket.
"""
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404


def basket_contents(request):
    """
    Returns the contents of the basket.
    """

    basket_items = []
    total = 0
    product_count = 0

    # Delivery variables demonstration from Code Institute Boutique Ado
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
