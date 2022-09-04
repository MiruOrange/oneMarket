from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.form import CustomerForm
from myapp.models import product

# Create your views here.

def index(request):
    index =[0, 1, 2, 3, 4, 5, 6, 7] #給商品圖使用的索引值
    return render(request, 'index.html', locals())


