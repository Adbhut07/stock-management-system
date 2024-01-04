from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from MyApp.models import *
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def Hello(request):
	msg="Welcome to My Django"
	return HttpResponse(msg)

def login(request):
	return render(request,'login.html')
@csrf_exempt
def logincheck(request):
	a=request.POST.get("sname")
	b=request.POST.get("spass")
	if a=="adbhut" and b=="12345":
		return render(request,'useradmin.html')
	else:
		msg="login failed 😔"
	return HttpResponse(msg)

def useradmin(request):
	return render(request,'useradmin.html')


def index1(request):
	return render(request,'index1.html')

def storeinsert(request):
	return render(request,'storeinsert.html')
def storefind(request):
	return render(request,'storefind.html')
def storedelete(request):
	return render(request,'storedelete.html')
def storeupdate(request):
	return render(request,'storeupdate.html')

def pcatinsert(request):
	return render(request,'pcatinsert.html')
def pcatfind(request):
	return render(request,'pcatfind.html')
def pcatdelete(request):
	return render(request,'pcatdelete.html')
def pcatupdate(request):
	return render(request,'pcatupdate.html')

def productinsert(request):
	return render(request,'productinsert.html')
def productfind(request):
	return render(request,'productfind.html')
def productdelete(request):
	return render(request,'productdelete.html')
def productupdate(request):
	return render(request,'productupdate.html')

def supplierinsert(request):
	return render(request,'supplierinsert.html')
def supplierfind(request):
	return render(request,'supplierfind.html')
def supplierdelete(request):
	return render(request,'supplierdelete.html')
def supplierupdate(request):
	return render(request,'supplierupdate.html')

def stockininsert(request):
	return render(request,'stockininsert.html')
def stockinfind(request):
	return render(request,'stockinfind.html')
def stockindelete(request):
	return render(request,'stockindelete.html')
def stockinupdate(request):
	return render(request,'stockinupdate.html')

def custinsert(request):
	return render(request,'custinsert.html')
def custfind(request):
    return render(request,'custfind.html')
def custdelete(request):
	return render(request,'custdelete.html')
def custupdate(request):
	return render(request,'custupdate.html')

def ordersinsert(request):
	return render(request,'ordersinsert.html')
def ordersfind(request):
	return render(request,'ordersfind.html')
def ordersdelete(request):
	return render(request,'ordersdelete.html')
def ordersupdate(request):
	return render(request,'ordersupdate.html')

def billinsert(request):
	return render(request,'billinsert.html')
def billfind(request):
	return render(request,'billfind.html')
def billdelete(request):
	return render(request,'billdelete.html')
def billupdate(request):
	return render(request,'billupdate.html')


@csrf_exempt
def orderssave(request):
	a=request.POST.get("oid")
	b=request.POST.get("cid")
	c=request.POST.get("pid")
	d=request.POST.get("pcid")
	e=request.POST.get("qty")
	f=request.POST.get("date")
	obj=orders(orderid=a,custid=b,pid=c,pcatid=d,quantity=e,dateoforder=f)
	obj.save()
	return render(request,'ormessage1.html')
	return HttpResponse(msg)

@csrf_exempt
def orderssearch(request):
	a=request.POST.get("oid")
	obj=orders.objects.filter(orderid=a)
	dt={'oid':obj[0].orderid,'cid':obj[0].custid,'pid':obj[0].pid,'pcid':obj[0].pcatid,'qty':obj[0].quantity,'date':obj[0].dateoforder}
	context={'data':dt}
	return render(request,'ordersfind.html',context)
	
@csrf_exempt
def orderdelete(request):
	a=request.POST.get("oid")
	obj=orders.objects.get(orderid=a)
	obj.delete()
	return render(request,'ormessage2.html')
	return HttpResponse(msg)

@csrf_exempt
def orderupdate(request):
	a=request.POST.get("oid")
	b=request.POST.get("cid")
	c=request.POST.get("pid")
	d=request.POST.get("pcid")
	e=request.POST.get("qty")
	f=request.POST.get("date")
	obj=orders.objects.get(orderid=a)
	obj.custid=b
	obj.pid=c
	obj.pcatid=d
	obj.quantity=e
	obj.dateoforder=f
	obj.save()
	return render(request,'ormessage3.html')
	return HttpResponse(msg)

@csrf_exempt
def pcatsave(request):
	a=request.POST.get("pcid")
	b=request.POST.get("sname")
	c=request.POST.get("desc")
	obj=productcat(pcatid=a,catname=b,desc=c)
	obj.save()
	return render(request,'pcmessage1.html')
	return HttpResponse(msg)

@csrf_exempt
def pcatsearch(request):
	a=request.POST.get("pcid")
	obj=productcat.objects.filter(pcatid=a)
	msg="<table border='1' width='100%'>"
	msg=msg+"<tr>"
	msg=msg+"<th>pcatid</td>"
	msg=msg+"<th>catname/td>"
	msg=msg+"<th>desc</td>"
	msg=msg+"</tr>"
	for r in obj:
		msg=msg+"<tr>"
		msg=msg+"<td>"+r.pcatid+"</td>"
		msg=msg+"<td>"+r.catname+"</td>"
		msg=msg+"<td>"+r.desc+"</td>"
		msg=msg+"</tr>"
	msg=msg+"</table>"
	return HttpResponse(msg)

@csrf_exempt
def pcdelete(request):
	a=request.POST.get("pcid")
	obj=productcat.objects.get(pcatid=a)
	obj.delete()
	return render(request,'pcmessage2.html')
	return HttpResponse(msg)

@csrf_exempt
def pcupdate(request):
	a=request.POST.get("pcid")
	b=request.POST.get("sname")
	c=request.POST.get("desc")
	obj=productcat.objects.get(pcatid=a)
	obj.catname=b
	obj.desc=c
	obj.save()
	return render(request,'pcmessage3.html')
	return HttpResponse(msg)

@csrf_exempt
def productssave(request):
	a=request.POST.get("pid")
	b=request.POST.get("pcid")
	c=request.POST.get("sname")
	d=request.POST.get("unit")
	e=request.POST.get("sprice")
	f=request.POST.get("oqty")
	g=request.POST.get("cqty")
	obj=products(pid=a,pcatid=b,productname=c,unit=d,priceperunit=e,openqty=f,currentqty=g)
	obj.save()
	return render(request,'pmessage1.html')
	return HttpResponse(msg)

@csrf_exempt
def productssearch(request):
	a=request.POST.get("pid")
	obj=products.objects.filter(pid=a)
	msg="<table border='1' width='100%'>"
	msg=msg+"<tr>"
	msg=msg+"<th>pidid</td>"
	msg=msg+"<th>pcatid/td>"
	msg=msg+"<th>productname</td>"
	msg=msg+"<th>unit</td>"
	msg=msg+"<th>priceperunit</td>"
	msg=msg+"<th>openqty</td>"
	msg=msg+"<th>currentqty</td>"
	msg=msg+"</tr>"
	for r in obj:
		msg=msg+"<tr>"
		msg=msg+"<td>"+r.pid+"</td>"
		msg=msg+"<td>"+r.pcatid+"</td>"
		msg=msg+"<td>"+r.productname+"</td>"
		msg=msg+"<td>"+r.unit+"</td>"
		msg=msg+"<td>"+r.priceperunit+"</td>"
		msg=msg+"<td>"+r.openqty+"</td>"
		msg=msg+"<td>"+r.currentqty+"</td>"
		msg=msg+"</tr>"
	msg=msg+"</table>"
	return HttpResponse(msg)

@csrf_exempt
def pdelete(request):
	a=request.POST.get("pid")
	obj=products.objects.get(pid=a)
	obj.delete()
	return render(request,'pmessage2.html')
	return HttpResponse(msg)

@csrf_exempt
def pupdate(request):
	a=request.POST.get("pid")
	b=request.POST.get("pcid")
	c=request.POST.get("sname")
	d=request.POST.get("unit")
	e=request.POST.get("sprice")
	f=request.POST.get("oqty")
	g=request.POST.get("cqty")
	obj=products.objects.get(pid=a)
	obj.pcatid=b
	obj.productname=c
	obj.unit=d
	obj.priceperunit=e
	obj.openqty=f
	obj.currentqty=g
	obj.save()
	return render(request,'pmessage3.html')
	return HttpResponse(msg)


@csrf_exempt
def stockinsave(request):
	a=request.POST.get("sid")
	b=request.POST.get("pid")
	c=request.POST.get("pcid")
	d=request.POST.get("spid")
	e=request.POST.get("date")
	f=request.POST.get("qty")
	obj=stockin(stockinid=a,pid=b,pcatid=c,supid=d,datein=e,quantity=f)
	obj.save()
	return render(request,'simessage1.html')
	return HttpResponse(msg)

@csrf_exempt
def stockinsearch(request):
	a=request.POST.get("sid")
	obj=stockin.objects.filter(stockinid=a)
	msg="<table border='1' width='100%'>"
	msg=msg+"<tr>"
	msg=msg+"<th>stockinid</td>"
	msg=msg+"<th>pid/td>"
	msg=msg+"<th>pcatid</td>"
	msg=msg+"<th>supid</td>"
	msg=msg+"<th>datein</td>"
	msg=msg+"<th>quantity</td>"
	msg=msg+"</tr>"
	for r in obj:
		msg=msg+"<tr>"
		msg=msg+"<td>"+r.stockinid+"</td>"
		msg=msg+"<td>"+r.pid+"</td>"
		msg=msg+"<td>"+r.pcatid+"</td>"
		msg=msg+"<td>"+r.supid+"</td>"
		msg=msg+"<td>"+r.datein+"</td>"
		msg=msg+"<td>"+r.quantity+"</td>"
		msg=msg+"</tr>"
	msg=msg+"</table>"
	return HttpResponse(msg)

@csrf_exempt
def sidelete(request):
	a=request.POST.get("sid")
	obj=stockin.objects.get(stockinid=a)
	obj.delete()
	return render(request,'simessage2.html')
	return HttpResponse(msg)

@csrf_exempt
def siupdate(request):
	a=request.POST.get("sid")
	b=request.POST.get("pid")
	c=request.POST.get("pcid")
	d=request.POST.get("spid")
	e=request.POST.get("date")
	f=request.POST.get("qty")
	obj=stockin.objects.get(stockinid=a)
	obj.pid=b
	obj.pcatid=c
	obj.supid=d
	obj.datein=e
	obj.quantity=f
	obj.save()
	return render(request,'simessage3.html')
	return HttpResponse(msg)

@csrf_exempt
def storesave(request):
	a=request.POST.get("stid")
	b=request.POST.get("sname")
	c=request.POST.get("sadd")
	d=request.POST.get("sphone")
	e=request.POST.get("semail")
	f=request.POST.get("sgst")
	g=request.POST.get("span")
	obj=stores(storeid=a,storename=b,storeadd=c,phone=d,email=e,gst=f,pan=g)
	obj.save()
	return render(request,'stmessage1.html')
	return HttpResponse(msg)

@csrf_exempt
def storesearch(request):
	a=request.POST.get("stid")
	obj=stores.objects.filter(storeid=a)
	msg="<table border='1' width='100%'>"
	msg=msg+"<tr>"
	msg=msg+"<th>storeid</td>"
	msg=msg+"<th>storename/td>"
	msg=msg+"<th>storeadd</td>"
	msg=msg+"<th>phone</td>"
	msg=msg+"<th>email</td>"
	msg=msg+"<th>gst</td>"
	msg=msg+"<th>pan</td>"
	msg=msg+"</tr>"
	for r in obj:
		msg=msg+"<tr>"
		msg=msg+"<td>"+r.storeid+"</td>"
		msg=msg+"<td>"+r.storename+"</td>"
		msg=msg+"<td>"+r.storeadd+"</td>"
		msg=msg+"<td>"+r.phone+"</td>"
		msg=msg+"<td>"+r.email+"</td>"
		msg=msg+"<td>"+r.gst+"</td>"
		msg=msg+"<td>"+r.pan+"</td>"
		msg=msg+"</tr>"
	msg=msg+"</table>"
	return HttpResponse(msg)

@csrf_exempt
def stdelete(request):
	a=request.POST.get("stid")
	obj=stores.objects.get(storeid=a)
	obj.delete()
	return render(request,'stmessage2.html')
	return HttpResponse(msg)


@csrf_exempt
def stupdate(request):
	a=request.POST.get("stid")
	b=request.POST.get("sname")
	c=request.POST.get("sadd")
	d=request.POST.get("sphone")
	e=request.POST.get("semail")
	f=request.POST.get("sgst")
	g=request.POST.get("span")
	obj=stores.objects.get(storeid=a)
	obj.storename=b
	obj.storeadd=c
	obj.phone=d
	obj.email=e
	obj.gst=f
	obj.pan=g
	obj.save()
	return render(request,'stmessage3.html')
	return HttpResponse(msg)

@csrf_exempt
def suppliersave(request):
	a=request.POST.get("spid")
	b=request.POST.get("sname")
	c=request.POST.get("sadd")
	d=request.POST.get("sphone")
	e=request.POST.get("semail")
	obj=suppliers(supid=a,supname=b,supadd=c,phone=d,email=e)
	obj.save()
	return render(request,'spmessage1.html')
	return HttpResponse(msg)

@csrf_exempt
def suppliersearch(request):
	a=request.POST.get("spid")
	obj=suppliers.objects.filter(supid=a)
	msg="<table border='1' width='100%'>"
	msg=msg+"<tr>"
	msg=msg+"<th>supid</td>"
	msg=msg+"<th>supname</td>"
	msg=msg+"<th>supadd</td>"
	msg=msg+"<th>phone</td>"
	msg=msg+"<th>email</td>"
	msg=msg+"</tr>"
	for r in obj:
		msg=msg+"<tr>"
		msg=msg+"<td>"+r.supid+"</td>"
		msg=msg+"<td>"+r.supname+"</td>"
		msg=msg+"<td>"+r.supadd+"</td>"
		msg=msg+"<td>"+r.phone+"</td>"
		msg=msg+"<td>"+r.email+"</td>"
		msg=msg+"</tr>"
	msg=msg+"</table>"
	return HttpResponse(msg)


@csrf_exempt
def supdelete(request):
	a=request.POST.get("spid")
	obj=suppliers.objects.get(supid=a)
	obj.delete()
	return render(request,'spmessage2.html')
	return HttpResponse(msg)

@csrf_exempt
def supupdate(request):
	a=request.POST.get("spid")
	b=request.POST.get("sname")
	c=request.POST.get("sadd")
	d=request.POST.get("sphone")
	e=request.POST.get("semail")
	obj=suppliers.objects.get(supid=a)
	obj.supname=b
	obj.supadd=c
	obj.phone=d
	obj.email=e
	obj.save()
	return render(request,'spmessage3.html')
	return HttpResponse(msg)

@csrf_exempt
def custsave(request):
	a=request.POST.get("cid")
	b=request.POST.get("sname")
	c=request.POST.get("semail")
	d=request.POST.get("sphone")
	e=request.POST.get("sadd")
	f=request.POST.get("scity")
	obj=customers(custid=a,custname=b,email=c,phone=d,custadd=e,custcity=f)
	obj.save()
	return render(request,'cmessage1.html')
	return HttpResponse(msg)


@csrf_exempt
def custsearch(request):
	a=request.POST.get("cid")
	obj=customers.objects.filter(custid=a)
	msg="<table border='1' width='100%'>"
	msg=msg+"<tr>"
	msg=msg+"<th>custdid</td>"
	msg=msg+"<th>custname</td>"
	msg=msg+"<th>email</td>"
	msg=msg+"<th>phone</td>"
	msg=msg+"<th>custadd</td>"
	msg=msg+"<th>custcity</td>"
	msg=msg+"</tr>"
	for r in obj:
		msg=msg+"<tr>"
		msg=msg+"<td>"+r.custid+"</td>"
		msg=msg+"<td>"+r.custname+"</td>"
		msg=msg+"<td>"+r.email+"</td>"
		msg=msg+"<td>"+r.phone+"</td>"
		msg=msg+"<td>"+r.custadd+"</td>"
		msg=msg+"<td>"+r.custcity+"</td>"
		msg=msg+"</tr>"
	msg=msg+"</table>"
	return HttpResponse(msg)

@csrf_exempt
def customersdelete(request):
	a=request.POST.get("cid")
	obj=customers.objects.get(custid=a)
	obj.delete()
	return render(request,'cmessage2.html')
	return HttpResponse(msg)

@csrf_exempt
def customerupdate(request):
	a=request.POST.get("cid")
	b=request.POST.get("sname")
	c=request.POST.get("semail")
	d=request.POST.get("sphone")
	e=request.POST.get("sadd")
	f=request.POST.get("scity")
	obj=customers.objects.get(custid=a)
	obj.custname=b
	obj.email=c
	obj.pohone=d
	obj.custadd=e
	obj.custcity=f
	obj.save()
	return render(request,'cmessage3.html')
	return HttpResponse(msg)

@csrf_exempt
def billsave(request):
	a=request.POST.get("bid")
	b=request.POST.get("oid")
	c=request.POST.get("cid")
	d=request.POST.get("pid")
	e=request.POST.get("pcid")
	f=request.POST.get("qty")
	g=request.POST.get("date")
	h=request.POST.get("samount")
	obj=bills(billid=a,orderid=b,custid=c,pid=d,pcatid=e,quantity=f,dateofbill=g,amount=h)
	obj.save()
	return render(request,'bmessage1.html')
	return HttpResponse(msg)

@csrf_exempt
def billsearch(request):
	a=request.POST.get("bid")
	obj=bills.objects.filter(billid=a)
	msg="<table border='1' width='100%'>"
	msg=msg+"<tr>"
	msg=msg+"<th>billid</td>"
	msg=msg+"<th>orderid</td>"
	msg=msg+"<th>custid</td>"
	msg=msg+"<th>pid</td>"
	msg=msg+"<th>pcatid</td>"
	msg=msg+"<th>quantity</td>"
	msg=msg+"<th>dateofbill</td>"
	msg=msg+"<th>amount</td>"
	msg=msg+"</tr>"
	for r in obj:
		msg=msg+"<tr>"
		msg=msg+"<td>"+r.billid+"</td>"
		msg=msg+"<td>"+r.orderid+"</td>"
		msg=msg+"<td>"+r.custid+"</td>"
		msg=msg+"<td>"+r.pid+"</td>"
		msg=msg+"<td>"+r.pcatid+"</td>"
		msg=msg+"<td>"+r.quantity+"</td>"
		msg=msg+"<td>"+r.dateofbill+"</td>"
		msg=msg+"<td>"+r.amount+"</td>"
		msg=msg+"</tr>"
	msg=msg+"</table>"
	return HttpResponse(msg)

@csrf_exempt
def bdelete(request):
	a=request.POST.get("bid")
	obj=bills.objects.get(billid=a)
	obj.delete()
	return render(request,'bmessage2.html')
	return HttpResponse(msg)


@csrf_exempt
def bupdate(request):
	a=request.POST.get("bid")
	b=request.POST.get("oid")
	c=request.POST.get("cid")
	d=request.POST.get("pid")
	e=request.POST.get("pcid")
	f=request.POST.get("qty")
	g=request.POST.get("date")
	h=request.POST.get("samount")
	obj=bills.objects.get(billid=a)
	obj.orderid=b
	obj.custid=c
	obj.pid=d
	obj.pcatid=e
	obj.quantity=f
	obj.dateofbill=g
	obj.amount=h
	obj.save()
	return render(request,'bmessage3.html')
	return HttpResponse(msg)



def login12(request):
	form = UserCreationForm()
	if request.method =='POST':
		form= UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
	context = {'form':form}
	return render(request,'login12.html',context)