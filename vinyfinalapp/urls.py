from django.conf.urls import url
from vinyfinalapp import views
from vinyfinalapp.views import BeforeLogIn,LogIn,Register,Saveuser, Loadupdate, Updateuser, CategoryList, ShowMain, ProductList, AddCartList, Signout
from vinyfinalapp.models import vinyusers,vinyproducts

urlpatterns = [
    url(r'^login/$', views.BeforeLogIn, name='Signin'),
	url(r'^aftrlogin/$', views.LogIn, name='Login'),
	url(r'^reg/$', views.Register, name='Register'),
	url(r'^saveusr/$', views.Saveuser, name='SaveUser'),
	url(r'^loadupdt/$', views.Loadupdate, name='Loadupdate'),
	url(r'^updtusr/$', views.Updateuser, name='UpdateUser'),
	url(r'^ctgr/$', views.CategoryList, name='Category'),
	url(r'^main/$', views.ShowMain, name='Showmain'),
	url(r'^prdcts/$', views.ProductList, name='Products'),
	url(r'^addcart/$', views.AddCartList, name='AddCart'),
	url(r'^signout/$', views.Signout, name='Signout')]