"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Hello/',Hello),
    path('login/',login),
    path('logincheck/',logincheck),
    path('useradmin/',useradmin),
    path('index1/',index1),
    path('storeinsert/',storeinsert),
    path('storefind/',storefind),
    path('storedelete/',storedelete),
    path('storeupdate/',storeupdate),
    path('pcatinsert/',pcatinsert),
    path('pcatfind/',pcatfind),
    path('pcatdelete/',pcatdelete),
    path('pcatupdate/',pcatupdate),
    path('productinsert/',productinsert),
    path('productfind/',productfind),
    path('productdelete/',productdelete),
    path('productupdate/',productupdate),
    path('supplierinsert/',supplierinsert),
    path('supplierfind/',supplierfind),
    path('supplierdelete/',supplierdelete),
    path('supplierupdate/',supplierupdate),
    path('stockininsert/',stockininsert),
    path('stockinfind/',stockinfind),
    path('stockindelete/',stockindelete),
    path('stockinupdate/',stockinupdate),
    path('custinsert/',custinsert),
    path('custfind/',custfind),
    path('custdelete/',custdelete),
    path('custupdate/',custupdate),
    path('ordersinsert/',ordersinsert),
    path('ordersfind/',ordersfind),
    path('ordersdelete/',ordersdelete),
    path('ordersupdate/',ordersupdate),
    path('billinsert/',billinsert),
    path('billfind/',billfind),
    path('billdelete/',billdelete),
    path('billupdate/',billupdate),
    path('orderssave/',orderssave),
    path('orderssearch/',orderssearch),
    path('orderdelete/',orderdelete),
    path('orderupdate/',orderupdate),
    path('pcatsave/',pcatsave),
    path('pcatsearch/',pcatsearch),
    path('pcdelete/',pcdelete),
    path('pcupdate/',pcupdate),
    path('productssave/',productssave),
    path('productssearch/',productssearch),
    path('pdelete/',pdelete),
    path('pupdate/',pupdate),
    path('stockinsave/',stockinsave),
    path('stockinsearch/',stockinsearch),
    path('sidelete/',sidelete),
    path('siupdate/',siupdate),
    path('storesave/',storesave),
    path('storesearch/',storesearch),
    path('stdelete/',stdelete),
    path('stupdate/',stupdate),
    path('suppliersave/',suppliersave),
    path('suppliersearch/',suppliersearch),
    path('supdelete/',supdelete),
    path('supupdate/',supupdate),
    path('custsave/',custsave),
    path('custsearch/',custsearch),
    path('customersdelete/',customersdelete),
    path('customerupdate/',customerupdate),
    path('billsave/',billsave),
    path('billsearch/',billsearch),
    path('bdelete/',bdelete),
    path('bupdate/',bupdate),


    path('login12/',login12)

    




]
