from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('contact_page', views.contact_page),
    path('services_page', views.services_page),
    path('reviews_page', views.reviews_page),
    path('about_us_page', views.about_us_page),
]