from nturl2path import url2pathname
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('properties', views.properties, name='properties'),
    path('property', views.property, name='property'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('contact', views.contact, name='contact'),
]