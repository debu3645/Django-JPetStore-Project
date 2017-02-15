from __future__ import unicode_literals

from django.db import models

# Create your models here.

class vinyusers(models.Model):
	vuser = models.CharField(max_length=10, null=True)
	vpassword = models.CharField(max_length=10, null=True)
	
class vinyproducts(models.Model):
	vpid = models.CharField(max_length=10, null=True)
	vpname = models.CharField(max_length=20, null=True)
	vptype = models.CharField(max_length=10, null=True)
	 
class vinyitems(models.Model):
	vpid = models.CharField(max_length=10, null=True)
	vitemid = models.CharField(max_length=20, null=True)
	vdesc = models.CharField(max_length=50, null=True)
	vprice = models.FloatField(default=0.0)

class vinyaddcart(models.Model):
	vpid = models.CharField(max_length=10, null=True)
	vitemid = models.CharField(max_length=20, null=True)
	vdesc = models.CharField(max_length=50, null=True)
	vprice = models.FloatField(default=0.0)
	vstock = models.CharField(max_length=10,default='true')
	quantity = models.IntegerField(default=1)
	

