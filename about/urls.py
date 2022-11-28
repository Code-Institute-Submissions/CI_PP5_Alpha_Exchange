"""
A Module to hold all the URL's for the about app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
]
