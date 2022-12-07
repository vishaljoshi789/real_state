from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('properties', views.properties, name='properties'),
    path('property', views.property, name='property'),
    path('add-wishlist/<int:property_id>', views.add_wishlist, name='add_wishlist'),
    path('contact', views.contact, name='contact'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('register', views.register, name='register'),
    path('wishlists', views.get_wishlists, name='get_wishlists'),
]