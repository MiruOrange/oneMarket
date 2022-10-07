from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index), 
    path('index/', views.index),  #首頁
    path('userlogin/',views.userlogin), #登入會員
    path('useradd/',views.useradd), #註冊會員
    path('detail/<int:id>/', views.detail),
    path('cart/', views.cart),
    path('addtocart/<str:type>/<int:id>/', views.addtocart),
    path('addtocart/<str:type>/', views.addtocart),
    path('menu/', views.menu),
    path('cartorder/', views.cartorder),
    path('cartok/', views.cartok),
    path('userlogout/', views.userlogout),
]
