from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index,name='index'),
    path('admin1/',views.admin1, name='admin1'),
    path('admintable/',views.admintable, name='admintable'),
    path('adminreg/',views.adminreg, name='adminreg'),
    path('admindel/<int:dataid>',views.admindel,name="admindel"),
    path('adminupdt/<int:dataid>',views.adminupdt,name="adminupdt"),
    path('updating/<int:dataid>',views.updating,name="updating"),
    path('prodlist/',views.prodlist,name='prodlist')

]