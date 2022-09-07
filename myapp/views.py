from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import ProductModel, OrderModel, DetailModel

# Create your views here.

def index(request):
    products = ProductModel.objects.all()
    return render(request, 'index.html', locals())

def userlogin(request):
    # return HttpResponse("測試")
    useradd_success_status=False #只有登入
    return render(request, 'userlogin.html', locals())

def useradd(request):
    if request.method == "POST":
        username = request.POST['username']
        userPassword = request.POST['userPassword']
        userRePassword = request.POST['userRePassword']
        userPhone = request.POST['userPhone']
        userBirthday = request.POST['userBirthday']
        userEmail = request.POST['userEmail']

        print(username)
        print(userPassword)
        print(userRePassword)
        print(userPhone)
        print(userBirthday)

        #判斷是否登入
        try:
            user=User.objects.get(username=username)  
        except:
            user=None
        
        if user!=None:
            print("帳號已建立")
            password_check=True #密碼檢查
            return render(request, "useradd2.html",locals())  
        else:
            if userPassword != userRePassword:
                password_check=False
                return render(request, "useradd2.html",locals())  
            else:
                print("可註冊")
                #儲存至資料庫
                user = User.objects.create_user(username, userEmail, userPassword)
                user.is_staff = False	# 工作人員狀態，設定True則可以登入admin後台
                user.is_active = True
                user.tel = userPhone
                user.cBirthday = userBirthday
                user.save()
                useradd_success_status=True #註冊成功
                return render(request, "userlogin.html",locals())
    else:
        user=None #註冊帳號檢查
        password_check=True #密碼檢查
        return render(request, "useradd2.html",locals()) 
    # return HttpResponse("測試")

def detail(request, id=None):
    product = ProductModel.objects.get(id=id)
    return render(request, 'detail.html', locals())

def addtocart(request, id):
    return HttpResponse(id)
    
