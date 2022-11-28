"""
A Module to handle the Stripe webhook
"""
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem
from products.models import Product
from users.models import UserAccount
import json
import time


class StripeWH_Handler:
    """
    Class to handle Stripe webhooks.
    """

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
        Send the user a confirmation email
        """
        custom_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_emails_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_emails_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [custom_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event.
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle successful payments from the webhook.
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        ship_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in ship_details.address.items():
            if value == "":
                ship_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserAccount.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = ship_details.phone
                profile.default_street_address1 = ship_details.address.line1
                profile.default_street_address2 = ship_details.address.line2
                profile.default_town_or_city = ship_details.address.city
                profile.default_county = ship_details.address.state
                profile.default_postcode = ship_details.address.postal_code
                profile.default_country = ship_details.address.country
                profile.save()

        # check if the order already exists in teh database
        order_exists = False
        attempt = 1
        # check 5 times after 1 second sleep
        while attempt <= 5:
            try:
                # order exists get details
                order = Order.objects.get(
                    full_name__iexact=ship_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=ship_details.phone,
                    street_address1__iexact=ship_details.address.line1,
                    street_address2__iexact=ship_details.address.line2,
                    town_or_city__iexact=ship_details.address.city,
                    county__iexact=ship_details.address.state,
                    postcode__iexact=ship_details.address.postal_code,
                    country__iexact=ship_details.address.country,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                # order does not exist, sleep and increment
                attempt += 1
                time.sleep(1)
        if order_exists:
            # call send email and respond to webhook
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]}' +
                " | SUCCESS: Verified order already in database",
                status=200)
        else:
            order = None
            try:
                # order doesn't exist after 5 seconds create it anyway
                order = Order.objects.create(
                    full_name=ship_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=ship_details.phone,
                    country=ship_details.address.country,
                    postcode=ship_details.address.postal_code,
                    town_or_city=ship_details.address.city,
                    street_address1=ship_details.address.line1,
                    street_address2=ship_details.address.line2,
                    county=ship_details.address.state,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                # list the items on the order by size if applicable
                for item_id, item_data in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['item_sizes'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            # server error occurred, send error response
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        # send email confirmation before successful server response
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}' +
            " | SUCCESS: Created order in webhook",
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle failed payments from the webhook.
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
