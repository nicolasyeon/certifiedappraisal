from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# from dotenv import load_dotenv
# import bcrypt
import requests
import json
import geocoder
import os

# load_dotenv()

def index(request):
    return render(request, 'index.html')

def contact_page(request):
    return render(request, 'contact.html')

def services_page(request):
    return render(request, 'services.html')

def reviews_page(request):
    return render(request, 'reviews.html')

def about_us_page(request):
    return render(request, 'about_us.html')