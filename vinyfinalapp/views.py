from django.shortcuts import render
from vinyfinalapp.models import vinyusers , vinyproducts, vinyitems, vinyaddcart
from django.core.cache import cache
import memcache
from django.db.models import Sum   # To calculate the sum of a column of a db table/model
from .forms import LoginForm, RegForm, NewAccForm, ProfileForm, CategoryForm, QuantityForm
# Create your views here.
#memc = memcache.Client(['127.0.0.1:11211'], debug=1)
def BeforeLogIn(request):
	form = LoginForm()
	return render(request, 'login.html',{'form':form},)

def LogIn(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		error_print = ""
		if form.is_valid():
			try:
				user = form.cleaned_data['User']
				password = form.cleaned_data['Password']
				vruser = vinyusers.objects.get(vuser=user)
				vrpassword = vinyusers.objects.get(vpassword=password)
			except:
				vruser = "null"
				vrpassword = "null"
				error_print = "User/Password Invalid.. Please try again"
			
			if vruser != "null" and vrpassword !="null":
				#memc = memcache.Client(['127.0.0.1:11211'], debug=1)
				cache.set('c1', user)
				cache.set('c2', password)
				form = LoginForm()				
				return render(request, 'index.html',{'form':form,'user':user, 'error_print' : error_print},)
			else:
				return render(request, 'login.html',{'form':form, 'error_print' : error_print},)
				
	#else:
		#form = LoginForm()
	return render(request, 'login.html',{'form':form, 'abc':vruser, 'def':vrpassword},) 

def Register(request):
	form = RegForm()
	form1 = NewAccForm()
	form2 = ProfileForm()
	return render(request, 'register.html',{'form':form, 'form1':form1, 'form2':form2},)

def Saveuser(request):
	if request.method == "POST":
		#form = RegForm()
		form1 = NewAccForm()
		form2 = ProfileForm()
		error_print = ""
		form = RegForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data['UserId']
			password = form.cleaned_data['Password']
			rpassword = form.cleaned_data['Repeatpassword']
				#vruser = vinyusers.objects.get(vuser=user)
			if password != rpassword:
				error_print = "Password and Repeast-Password doesnt match."
				#return render(request, 'register.html',{'form':form, 'form1':form1, 'form2':form2, 'error_print':error_print, 'password': password, 'rpassword':rpassword},)
			else:
				#error_print = ""
				try:
					vruser = vinyusers.objects.get(vuser=user)
					error_print = "User already exists.. try another user Id"
				except:
					#vruser = "null"
					crtusr =vinyusers(vuser=user, vpassword=password)
					crtusr.save()
					error_print = "user Id created successfully...."
					user = user
					
					cache.set('c1', user)
					cache.set('c2', password)
					return render(request, 'index.html',{'form':form,'user':user},)
	return render(request, 'register.html',{'form':form, 'form1':form1, 'form2':form2, 'error_print':error_print},)

def Updateuser(request):
	if request.method == "POST":
		#form = RegForm()
		form1 = NewAccForm()
		form2 = ProfileForm()
		error_print = ""
		form = RegForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data['UserId']
			password = form.cleaned_data['Password']
			#rpassword = form.cleaned_data['Repeatpassword']
			#vruser = vinyusers.objects.get(vuser=c11)
			#updtusr =vinyusers(vuser=user, vpassword=password)
			updtusr = vinyusers.objects.get(vuser=user)
			updtusr.vpassword = password
			updtusr.err_flag=1
			updtusr.save()
			error_print = "user Id update successfully...."			
			return render(request, 'update.html',{'form':form, 'form1':form1, 'form2':form2, 'error_print':error_print},)

def Loadupdate(request):
	form = RegForm()
	form1 = NewAccForm()
	form2 = ProfileForm()
	#memc = memcache.Client(['127.0.0.1:11211'], debug=1)
	c11 = cache.get('c1')
	c22 = cache.get('c2')
	#c11="Vineetc11"
	#c22="vineetc22"
	form.fields["UserId"].initial = c11
	form.fields["Password"].initial = c22
	return render(request, 'update.html',{'form':form, 'form1':form1, 'form2':form2, 'c11':c11, 'c22':c22})

def CategoryList(request):
	
	if request.method == "GET":	
		cgr = ""
		form = CategoryForm()
		if request.GET.get('value') == '1':
			cgr = "Fish"
		elif request.GET.get('value') == '2':
			cgr = "Dog"
		elif request.GET.get('value') == '3':
			cgr = "Reptiles" 
		elif request.GET.get('value') == '4':
			cgr = "Cats" 
		elif request.GET.get('value') == '5':
			cgr = "Birds" 
		vproducts = vinyproducts.objects.filter(vptype=cgr)
	return render(request, 'category.html',{'form':form, 'cgr':cgr, 'vproducts':vproducts})

def ShowMain(request):
	form = LoginForm()
	user = cache.get('c1')
	return render(request, 'index.html',{'form':form,'user':user},)
	
def ProductList(request):
	
	if request.method == "GET":	
		prdct = ""
		form = CategoryForm()
		prdct = request.GET.get('value')
		vitems = vinyitems.objects.filter(vpid=prdct)
		vproducts = vinyproducts.objects.get(vpid=prdct)
	return render(request, 'product.html',{'form':form, 'prdct':prdct, 'vitems':vitems, 'vproducts': vproducts})

def AddCartList(request):
	
	if request.method == "GET":	
		prdct = ""
		error_print = ""
		form = QuantityForm()
		prdct = request.GET.get('value')
		myitemid = request.GET.get('value2')
		vitems = vinyitems.objects.filter(vpid=prdct, vitemid=myitemid).values('vitemid')
		vproducts= vinyitems.objects.filter(vpid=prdct, vitemid=myitemid).values('vpid')
		vdescr= vinyitems.objects.filter(vpid=prdct, vitemid=myitemid).values('vdesc')
		vprices= vinyitems.objects.filter(vpid=prdct, vitemid=myitemid).values('vprice')
		vaddcart =vinyaddcart(vpid=vproducts[0]['vpid'], vitemid=vitems[0]['vitemid'], vdesc=vdescr[0]['vdesc'], vprice=vprices[0]['vprice'])
		vaddcart.save()
		error_print = "Item included in AddCartList"
		vmycart = vinyaddcart.objects.filter(vpid=prdct)
		vtot = vinyaddcart.objects.aggregate(Sum('vprice'))
	#return render(request, 'addcart.html',{'form':form, 'prdct':prdct,'vmycart':vmycart, 'error_print':error_print, 'myitemid':myitemid})
	return render(request, 'addcart.html',{'form':form,'error_print':error_print, 'vmycart':vmycart, 'vtot':vtot}, )

def Signout(request):
	form = LoginForm()
	cache.clear()
	return render(request, 'login.html',{'form':form},)