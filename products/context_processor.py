"""
Context Processor to create a list of all the categories.
"""
from .models import Category


def catslist(request):
    """
    Processes the catagories into a list.
    """
    categories = Category.objects.all()
    context = {
        'categories_list': categories
    }

    return context
