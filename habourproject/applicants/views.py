from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser


# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Talent Habour Web application.")
