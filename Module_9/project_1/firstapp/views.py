from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def contact(request):
    return HttpResponse("Contact page from firstapp/views.py")

def home(request):
    return HttpResponse("Home page from firstapp/views.py")