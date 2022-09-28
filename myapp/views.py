from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import ProductModel, OrderModel, DetailModel, User
from django.contrib import auth
from datetime import datetime
from django.contrib.auth import authenticate
from datetime import datetime, timedelta #cookie方式紀錄被瀏覽次數
from django.contrib.sessions.models import Session

# Create your views here.
cartlist = []  #用來存放選購的商品串列
shipping =100
count=0
counts=0
#如((苦無, 2000, 1, 2000), (血輪眼, 10000, 1, 10000), (軍糧丸, 2000, 1, 2000))
#    名稱，單價，數量，小計
def index(request):
    global count
    global counts
    products = ProductModel.objects.all()
    productlist = []
    for i in range(1, 9):
        product = ProductModel.objects.get(id = i)
        productlist.append(product)
    if request.user.is_authenticated: #設定登入後的驗證
        name=request.user.username
    #----增加用cookies方式記錄瀏覽次數----
    # if "counter" in request.COOKIES:
    #     count = int(request.COOKIES['counter'])
    #     count+=1
    #     # print(type(count))
        
    # else:
    #     count=1
    # response= render(request, 'index.html', locals())
    # tomorrow=datetime.now()+timedelta(days=1) #取出今天的時間後先將日期+1
    # tomorrow=datetime.replace(tomorrow,hour=8,minute=0,second=0) #再將時間重置成台灣(UTF+8)凌晨00:00:00
    # response.set_cookie(key='counter',value=count,expires=tomorrow) #設定cookies及到期時間
    # if "counters" in request.COOKIES:
    #     counts = int(request.COOKIES['counters'])
    #     counts+=1
    # #show_count=count #因經過response會導致global變數無法接收到數值，所以要放在response前面，global變數才會帶到資料
    # #show_counts=counts
    # variableDict=locals().copy() #創一個空字典變數承接=locals()!!因會把此"函式區域變數"變成字典方式丟去index.html
    # variableDict.update(globals()) #再把這個新變數裡面內容除了區域變數也把全域變數抓近來，再一起丟入index.html
    # response= render(request, 'index.html', variableDict)
    # expires=datetime.now()+timedelta(days=1) #取出今天的時間後先將日期+1
    # expires=datetime.replace(expires,hour=8,minute=0,second=0) #再將時間重置成台灣(UTF+8)凌晨00:00:00
    # response.set_cookie(key='counter',value=counts,expires=expires) #設定cookies及到期時間
    # response.set_cookie(key='counters',value=counts,expires=315360000) #設定cookies及到期時間
    # return response

    #---改用session方式紀錄瀏覽次數--
    if not "counter" in request.session:
        count =int(request.session['counter'])
        count+=1
        print(count)
        
    else:
         count=1
   
    tomorrow=datetime.now()+timedelta(days=1) #取出今天的時間後先將日期+1
    tomorrow=datetime.replace(tomorrow,hour=8,minute=0,second=0) #再將時間重置成台灣(UTF+8)凌晨00:00:00
    # request.session['']
    response.set_cookie(key='counter',value=count,expires=tomorrow) #設定cookies及到期時間
    # if "counters" in request.COOKIES:
    #     counts = int(request.COOKIES['counters'])
    #     counts+=1
    # #show_count=count #因經過response會導致global變數無法接收到數值，所以要放在response前面，global變數才會帶到資料
    # #show_counts=counts
    variableDict=locals().copy() #創一個空字典變數承接=locals()!!因會把此"函式區域變數"變成字典方式丟去index.html
    variableDict.update(globals()) #再把這個新變數裡面內容除了區域變數也把全域變數抓近來，再一起丟入index.html
    response= render(request, 'index.html', variableDict)
    # expires=datetime.now()+timedelta(days=1) #取出今天的時間後先將日期+1
    # expires=datetime.replace(expires,hour=8,minute=0,second=0) #再將時間重置成台灣(UTF+8)凌晨00:00:00
    # response.set_cookie(key='counter',value=counts,expires=expires) #設定cookies及到期時間
    # response.set_cookie(key='counters',value=counts,expires=315360000) #設定cookies及到期時間
    return response

   

def menu(request):
    global count
    global counts
    products = ProductModel.objects.all()
    return render(request, 'menu.html', locals())

def userlogin(request):
    global count
    global counts
    message=""
    if request.method == "POST":
        username = request.POST['username']
        userPassword = request.POST['userPassword']
        print(username+" "+userPassword)
        user = authenticate(username=username, password=userPassword) #password(資料庫裡面名稱ID)=userPassword(取得HTML前端使用者輸入的資料)
        if user is not None:
            auth.login(request, user)
            # message = "登入成功!"
            # print(conut)
            return redirect('/index/')
        else:
            message = "登入失敗!"
            return render(request, 'userlogin.html', locals())
    else:
    # return HttpResponse("測試")
        useradd_success_status=False #成功登入狀態=False 
        return render(request, 'userlogin.html', locals())

def useradd(request):
    if request.method == "POST":
        username = request.POST['username']
        userPassword = request.POST['userPassword']
        userRePassword = request.POST['userRePassword']
        userPhone = request.POST['userPhone']
        userBirthday = request.POST['userBirthday']
        userEmail = request.POST['userEmail']

        # print(username+" "+userPassword+" "+userRePassword+" "+userPhone+" "+userBirthday+" "+userEmail)
        # print(type(userBirthday)) #<class 'str'>
      
        #判斷是否登入
        try:
            user=User.objects.get(username=username)  
        except:
            user=None
        
        if user!=None: #帳號如果設定過就跳回useradd.html
            print("帳號已建立")
            password_check=True #密碼檢查
            return render(request, "useradd.html",locals())  
        else:
            if userPassword != userRePassword: #密碼跟確認密碼不同時跳回useradd.html
                password_check=False
                return render(request, "useradd.html",locals())  
            else:
                print("可註冊")
                #儲存至資料庫
                user = User.objects.create_user(username, userEmail, userPassword)
                user.is_staff = False	# 工作人員狀態，設定True則可以登入admin後台
                user.is_active = True   # True該用戶可登入
                user.cPhone = userPhone
                userBirthday=datetime.strptime(userBirthday,'%Y-%m-%d') #取得HTML的資料後因是字串，所以還要轉成物件
                # print(type(userBirthday)) #<class 'datetime.datetime'>
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
        noCartSession = True          #True，表示購物車session內沒有商品
        for unit in cartlist:                               #檢查購物車內是否已經有該品項商品，如果有，把數量加1
            if product.pname == unit[0]:                    #如果cartlist的session中有該選購商品的話
                unit[2] = str(int(unit[2])+1)               #商品數量加1
                unit[3] = str(int(unit[3])+product.pprice)  #購物車累計的商品金額，再加一筆商品單價，累計金額增加了
                noCartSession = False                                #表示購物車session內已經有商品了
                break
        if noCartSession:                                    #如果購物車內沒有商品
            templist = []    #暫時串列
            templist.append(product.pname)          #0的位置放入選購商品名稱
            templist.append(str(product.pprice))    #1的位置放入商品單價
            templist.append('1')                    #2的位置放入暫訂選購商品數量為1
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
        return redirect('/index/')
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
            

