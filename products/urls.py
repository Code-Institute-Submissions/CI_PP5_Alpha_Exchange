from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_products, name='all_products'),
    path('products/<int:page>/', views.list_products, name='all_products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('categories/', views.categories, name="categories"),
    path('categories_list/<str:cats>', views.categories_view,
         name="categories_list"),
]
