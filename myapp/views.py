from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.form import CustomerForm
from myapp.models import customer

# Create your views here.

def index(request):
    if request.method == 'POST':
        customerForm = CustomerForm(request.POST)
        if customerForm.is_valid():
            name = customerForm.cleaned_data['name']
            phone = customerForm.cleaned_data['phone']
            email = customerForm.cleaned_data['email']
            address = customerForm.cleaned_data['address']
            message = customerForm.cleaned_data['message']
            # itemAmount = request.POST['itemAmount']

            unit = customer.objects.create(name=name, phone=phone, email=email, address=address, message=message)
            unit.save()
            # redirect('/confirm/') 按下訂購鍵後導向訂購完成頁面，尚未完成。
    else:
        customerForm = CustomerForm()
    return render(request, 'index.html', locals())


