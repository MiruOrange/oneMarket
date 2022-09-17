from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import ProductModel, OrderModel, DetailModel, ProductCardModel

# Create your views here.
cartlist = []  #用來存放選購的商品串列
shipping =100
#如((苦無, 2000, 1, 2000), (血輪眼, 10000, 1, 10000), (軍糧丸, 2000, 1, 2000))

def index(request):
    products = ProductModel.objects.all()
    cardProducts = ProductCardModel.objects.all()
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

def detail(request,type=None ,id=None):
    if type =='carousel':
        product = ProductModel.objects.get(id=id)
    elif type =='card':
        product = ProductCardModel.objects.get(id=id)
    return render(request, 'detail.html', locals())

def addtocart(request, type=None, id=None):
    global cartlist      #取得session，裡面放著客戶選購的物品
    if type == 'add':
        product = ProductModel.objects.get(id=id)
        flag = True          #True，表示購物車session內沒有商品
        for unit in cartlist:                               #檢查購物車內是否已經有該品項商品，如果有，把數量加1
            if product.pname == unit[0]:                    #如果cartlist的session中有該選購商品的話
                unit[2] = str(int(unit[2])+1)               #商品數量加1
                unit[3] = str(int(unit[3])+product.pprice)  #購物車累計的商品金額，再加一筆商品單價，累計金額增加了
                flag = False                                #表示購物車session內已經有商品了
                break
        if flag:                                    #如果購物車內沒有商品
            templist = []    #暫時串列
            templist.append(product.pname)          #0的位置放入選購商品名稱
            templist.append(str(product.pprice))    #1的位置放入商品單價
            templist.append('1')                    #2的位置放入暫訂選購商品數量為1
            templist.append(str(product.pprice))    #3的位置放入暫訂選購商品總價
            cartlist.append(templist)   #將暫時串列，放入購物車的串列。
        request.session['cartlist']=cartlist    #將購物車放入串列
        return redirect('/cart/')

def cart (request):
    global cartlist
    global shipping
    cartlist1 = cartlist    #把cartlist轉成區域變數，要傳到cart.html
    localshipping = shipping
    total = 0
    for unit in cartlist:
        total = total +int(unit[3])  #第3個位置，固定存放目前累計的商品金額
    grandtotal = total + localshipping   #總價，要加上運費，最前面定義為100元。
    return render(request, 'cart.html', locals())
            

    
