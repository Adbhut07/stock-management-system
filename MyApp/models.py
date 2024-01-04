from django.db import models

# Create your models here.
class orders(models.Model):
	orderid=models.CharField(max_length=30)
	custid=models.CharField(max_length=30)
	pid=models.CharField(max_length=30)
	pcatid=models.CharField(max_length=30)
	quantity=models.CharField(max_length=30)
	dateoforder=models.CharField(max_length=30)
	class Meta:
		db_table='orders'

class productcat(models.Model):
	pcatid=models.CharField(max_length=30)
	catname=models.CharField(max_length=30)
	desc=models.CharField(max_length=30)
	class Meta:
		db_table='productcat'
class products(models.Model):
	pid=models.CharField(max_length=30)
	pcatid=models.CharField(max_length=30)
	productname=models.CharField(max_length=30)
	unit=models.CharField(max_length=30)
	priceperunit=models.CharField(max_length=30)
	openqty=models.CharField(max_length=30)
	currentqty=models.CharField(max_length=30)
	class Meta:
		db_table='products'

class stockin(models.Model):
	stockinid=models.CharField(max_length=30)
	pid=models.CharField(max_length=30)
	pcatid=models.CharField(max_length=30)
	supid=models.CharField(max_length=30)
	datein=models.CharField(max_length=30)
	quantity=models.CharField(max_length=30)
	class Meta:
		db_table='stockin'

class stores(models.Model):
	storeid=models.CharField(max_length=30)
	storename=models.CharField(max_length=30)
	storeadd=models.CharField(max_length=30)
	phone=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	gst=models.CharField(max_length=30)
	pan=models.CharField(max_length=30)
	class Meta:
		db_table='stores'

class suppliers(models.Model):
	supid=models.CharField(max_length=30)
	supname=models.CharField(max_length=30)
	supadd=models.CharField(max_length=30)
	phone=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	class Meta:
		db_table='suppliers'

class customers(models.Model):
	custid=models.CharField(max_length=30)
	custname=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	phone=models.CharField(max_length=30)
	custadd=models.CharField(max_length=30)
	custcity=models.CharField(max_length=30)
	class Meta:
		db_table='customers'

class bills(models.Model):
	billid=models.CharField(max_length=30)
	orderid=models.CharField(max_length=30)
	custid=models.CharField(max_length=30)
	pid=models.CharField(max_length=30)
	pcatid=models.CharField(max_length=30)
	quantity=models.CharField(max_length=30)
	dateofbill=models.CharField(max_length=30)
	amount=models.CharField(max_length=30)
	class Meta:
		db_table='bills'










