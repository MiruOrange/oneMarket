from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import ProductModel, OrderModel, DetailModel
import random

# Create your views here.
cartlist = []  #用來存放選購的商品串列
shipping =100
#如((苦無, 2000, 1, 2000), (血輪眼, 10000, 1, 10000), (軍糧丸, 2000, 1, 2000))
#    名稱，單價，數量，小計

def index(request):
    products = ProductModel.objects.all()
    productlist = []
    for i in range(1, 9):
        product = ProductModel.objects.get(id = i)
        productlist.append(product)
    return render(request, 'index.html', locals())

def menu(request):
    products = ProductModel.objects.all()
    return render(request, 'menu.html', locals())

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
        return render(request, "useradd.html",locals()) 
    # return HttpResponse("測試")

def detail(request,id=None):
    product = ProductModel.objects.get(id=id)
    return render(request, 'detail.html', locals())

def addtocart(request,type=None, id=None):  #這個函式負責新增或修改購物車的session內容
    global cartlist      #取得session，裡面放著客戶選購的物品
    if type == 'add':
        product = ProductModel.objects.get(id=id)
        quantity = request.POST['quantity']
        noCartSession = True          #True，表示購物車session內沒有商品
        for unit in cartlist:                               #檢查購物車內是否已經有該品項商品，如果有，把數量加1
            if product.pname == unit[0]:                    #如果cartlist的session中有該選購商品的話
                unit[2] = str(int(unit[2])+int(quantity))               #商品數量加1
                unit[3] = str(int(unit[3])+product.pprice)  #購物車累計的商品金額，再加一筆商品單價，累計金額增加了
                noCartSession = False                                #表示購物車session內已經有商品了
                break
        if noCartSession:                                    #如果購物車內沒有商品
            templist = []    #暫時串列
            templist.append(product.pname)          #0的位置放入選購商品名稱
            templist.append(str(product.pprice))    #1的位置放入商品單價
            templist.append(str(quantity))                    #2的位置放入暫訂選購商品數量為1
            templist.append(str(product.pprice))    #3的位置放入暫訂選購商品總價
            cartlist.append(templist)   #將暫時串列，放入購物車的串列。
        request.session['cartlist'] = cartlist      #將購物車的內容放入session
        return redirect('/cart/')
    elif type == 'update':
        n =0
        for unit in cartlist:
            #--這裡使用POST.get()的方法來接收前端傳來的資訊，與平時所習慣的POST['']不同
            #--但使用POST.get('')的好處不少
            #--1.如果前端傳來的資訊為空值，則POST[]會產生錯誤，POST.get()則會回傳None
            #--2.POST.get()，還可以設定default值，適合用在此處
            #--參考網頁 https://blog.csdn.net/geerniya/article/details/79761398
            unit[2] = request.POST.get('quantity'+str(n),'1')
            unit[3] = str(int(unit[1])*int(unit[2]))
            n += 1
        request.session['cartlist'] = cartlist  #更新cartlist的內容
        return redirect('/cart/')
    elif type == 'empty':
        cartlist = []
        request.session['cartlist'] = cartlist
        return redirect('/cart/')
    elif type == 'remove':
        del cartlist[int(id)]   #刪除指定位置的cartlist內容
        #---del內建語句，該語句不返回刪除的值。
        request.session['cartlist'] = cartlist
        return redirect('/cart/')

def cart (request):     #負責顯示購物車的內容
    global cartlist
    global shipping
    products = ProductModel.objects.all()
    cartlist1 = cartlist    #把cartlist轉成區域變數，要傳到cart.html
    localshipping = shipping
    total = 0
    for unit in cartlist:
        total = total +int(unit[3])  #第3個位置，固定存放目前累計的商品金額
    grandtotal = total + localshipping   #總價，要加上運費，最前面定義為100元。
    return render(request, 'cart.html', locals())

def cartorder(request):
    return render(request, 'cartorder.html', locals())
            

def cartorder(request):
    return render(request, 'cartorder.html', locals())
