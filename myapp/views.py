from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import ProductModel, OrderModel, DetailModel

# Create your views here.

def index(request):
    products = ProductModel.objects.all()
    return render(request, 'index.html', locals())


