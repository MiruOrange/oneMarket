from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.form import CustomerForm
from myapp.models import product

# Create your views here.

def index(request):
    return render(request, 'index.html', locals())


