from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_basket',
                       'stripe_pid')

    fields = ('full_name', 'street_address1', 'street_address2',
              'town_or_city', 'county', 'country',
              'postcode', 'email', 'phone_number',
              'order_number', 'date', 'delivery_cost',
              'order_total', 'grand_total', 'original_basket',
              'stripe_pid',)

    list_display = ('full_name', 'order_number', 'date',
                    'delivery_cost', 'order_total',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
