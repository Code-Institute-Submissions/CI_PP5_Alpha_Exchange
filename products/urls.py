from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_products, name='products')
]