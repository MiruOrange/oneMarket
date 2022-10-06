from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import ProductModel, OrderModel, DetailModel, User
from django.contrib import auth
from datetime import datetime
from django.contrib.auth import authenticate
from datetime import datetime, timedelta #cookie方式紀錄被瀏覽次數
from django.contrib.sessions.models import Session
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.text import MIMEText

# Create your views here.
cartlist = []  #用來存放選購的商品串列
shipping =100  #運費，設定為100。
message = ''
customername = ''
customerphone = ''
customeraddress = ''
customeremail = ''
#如((苦無, 2000, 1, 2000), (血輪眼, 10000, 1, 10000), (軍糧丸, 2000, 1, 2000))
#    名稱，單價，數量，小計
def index(request):
    global context
    products = ProductModel.objects.all() 
    productlist = []
    for i in range(1, 9):
        product = ProductModel.objects.get(id = i)
        productlist.append(product)
    if request.user.is_authenticated: #設定登入後的驗證
        name=request.user.username
    return render(request, 'index.html', locals())

   

def menu(request):
    products = ProductModel.objects.all()
    return render(request, 'menu.html', locals())

def userlogin(request):
    message=""
    if request.method == "POST":
        username = request.POST['username']
        userPassword = request.POST['userPassword']
        print(username+" "+userPassword)
        user = authenticate(username=username, password=userPassword) #password(資料庫裡面名稱ID)=userPassword(取得HTML前端使用者輸入的資料)
        loginstatus = False
        if user is not None:
            auth.login(request, user)
            # message = "登入成功!"
            # print(conut)
            request.User.is_authenticated
            return render(request, 'index.html', locals())
        else:
            message = "登入失敗!"
            return render(request, 'userlogin.html', locals())
    else:
    # return HttpResponse("測試")
        useradd_success_status=False #成功登入狀態=False 
        return render(request, 'userlogin.html', locals())

def userlogout(request):
    auth.logout(request)
    return redirect('/index/')

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
        quantity = int(request.POST['quantity'])    #將接收的數字轉成int後，放入quantity準備做計算使用
        noCartSession = True          #True，表示購物車session內沒有商品
        for unit in cartlist:                               #檢查購物車內是否已經有該品項商品，如果有，把數量加上選取數量
            if product.pname == unit[0]:                    #如果cartlist的session中有該選購商品的話
                unit[2] = str(int(unit[2])+int(quantity))               #商品數量加上所選取數量
                unit[3] = str(int(unit[3])+product.pprice*quantity)  #購物車累計的商品金額，再加一筆商品單價，累計金額增加了
                noCartSession = False                                #表示購物車session內已經有商品了
                break
        if noCartSession:                                    #如果購物車內沒有商品
            templist = []    #暫時串列
            templist.append(product.pname)          #0的位置放入選購商品名稱
            templist.append(str(product.pprice))    #1的位置放入商品單價
            templist.append(str(quantity))                    #2的位置放入顧客選購的數量
            templist.append(str(product.pprice*quantity))     #3的位置放入暫訂選購商品總價
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
    products = ProductModel.objects.all().order_by('?')[:2] #隨機排序並只取出2筆商品資訊
    cartlist1 = cartlist    #把cartlist轉成區域變數，要傳到cart.html
    localshipping = shipping
    total = 0
    for unit in cartlist:
        total = total +int(unit[3])  #第3個位置，固定存放目前累計的商品金額
    grandtotal = total + localshipping   #總價，要加上運費，最前面定義為100元。
    return render(request, 'cart.html', locals())

def cartorder(request):
    global cartlist, message, customername, customerphone, customeraddress, customeremail, shipping
    cartlist1 = cartlist    #將購物車的session轉成區域變數，準備傳到模版
    total = 0
    for unit in cartlist:
        total = total + int(unit[3])    #unit[3]放的是累計商品價格
    grandtotal = total + shipping       #總價=累計商品價格+運費
    shipping1 = shipping
    #--以下將所有顧客資料和要給顧客的訊息都傳到cartorder.html去
    message1 = message
    customername1 = customername
    customerphone1 = customerphone
    customeraddress1 = customeraddress
    customeremail1 = customeremail
    return render(request, 'cartorder.html', locals())

def cartok(request):
    global cartlist , message, customername, customerphone, customeraddress, customeremail, shipping
    if request.method == 'POST':
        total = 0
        for unit in cartlist:
            total = total +int(unit[3])
        grandtotal = total + shipping
        message = ''
        customername = request.POST['customername']
        customerphone = request.POST['customerphone']
        customeraddress = request.POST['customeraddress']
        customeremail = request.POST['customeremail']
        paytype = request.POST['paytype']
        localcustomername = customername    #放一個區域變數，要把顧客姓名傳到前端去顯示。
        #---將訂購人的資料寫進OrderModel裡------
        productorder = OrderModel.objects.create(subtotal = total, shipping = shipping, grandtotal = grandtotal , customername=customername, customerphone = customerphone, customeraddress = customeraddress, customeremail = customeremail, paytype = paytype)
        productorder.save()
        #---將該筆訂單的商品，寫進DetailModel裡-----
        #---因為預判商品項目不會只有一筆，所以用for迴圈來逐筆將商品放入資料庫---
        dtotal = 0
        for unit in cartlist:
            dtotal = int(unit[1])*int(unit[2])
            unitdetail = DetailModel.objects.create(dorder = productorder, pname = unit[0], unitprice = int(unit[1]), quantity = int(unit[2]), dtotal = dtotal)
            unitdetail.save()
        # return HttpResponse('傳送ok')
        cartlist = []   #在這裡清空購物車
        #郵件寄送-------------
        orderid = productorder.id
        mailfrom = 'maosicha014@gmail.com'
        mailpw = 'zhqhhihphxfmnpcw'
        mailto = customeremail
        mailsubject = '木葉商城-訂單成立通知'
        mailcontent = customername+'您好，感謝您的光臨。您的忍具已訂購成功！\n我們會盡速且祕密的把忍具送至您指定的地點。\n請在指定地點四周佈好木葉情報警戒結界，以確保您忍具的安全，感謝您的支持。'
        send_message(mailfrom, mailpw, mailto, mailsubject, mailcontent)
        #郵件寄送--------------------
        return render(request, 'cartok.html', locals())
    else:
        return HttpResponse('你的post有問題哦')

def send_message(mailfrom, mailpw, mailto, mailsubject, mailcontent):
    global message
    strSmtp = 'smtp.gmail.com:587'
    strAccount = mailfrom
    strPassword = mailpw
    msg = MIMEText(mailcontent)
    msg['Subject'] = mailsubject
    mailto1 = mailto
    server = SMTP(strSmtp)
    server.ehlo()
    server.starttls()
    try:
        server.login(strAccount, strPassword)
        server.sendmail(strAccount, mailto1, msg.as_string())
    except SMTPAuthenticationError:
        message ='無法登入'
    except:
        message ='郵件無法發送產生錯誤'
    server.quit()
            
