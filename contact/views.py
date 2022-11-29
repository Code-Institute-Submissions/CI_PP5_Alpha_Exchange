"""
A module containing the views within the contact app.
"""
from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def contact(request):
    """
    A view to contact us page with contact form,
    get contact details and save to model
    """
    contact_form = ContactForm()
    if request.method == 'GET':
        if not request.user.is_authenticated:
            contact_form = ContactForm()
        elif request.user.useraccount:
            contact_form = ContactForm(
                initial={
                    'name': request.user.useraccount.default_full_name,
                    'email': request.user.email,
                    'phone_number':
                        request.user.useraccount.default_phone_number,
                    'street_address1':
                        request.user.useraccount.default_street_address1,
                    'street_address2':
                        request.user.useraccount.default_street_address2,
                    'town_or_city':
                        request.user.useraccount.default_town_or_city,
                    'county': request.user.useraccount.default_county,
                    'postcode': request.user.useraccount.default_postcode,
                    'country': request.user.useraccount.default_country,
                }
            )
        else:
            contact_form = ContactForm(
                initial={
                    'email': request.user.email,
                        }
            )

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request, "Thank you for your message we"
                " will be in touch with you soon.")
    context = {'contact_form': contact_form, }

    return render(request, 'contact/contact.html', context)
