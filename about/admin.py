from django.contrib import admin
from .models import Faq


class FaqAdmin(admin.ModelAdmin):
    """
    Admin Class for Faq Model
    """
    list_display = ('friendly_title', 'question',)


admin.site.register(Faq, FaqAdmin)
