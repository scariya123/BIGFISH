from django.shortcuts import render,redirect
from .models import Admindb
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect



# Create your views here.
def index(request):
    return render(request, 'index.html')
def admin1(request):
    return render(request, 'admin.html')
def admintable(request):
    datas=Admindb.objects.all()
    return render(request,'admintable.html',{'datas':datas})
def adminreg(request):
    print("fffffffff")
    data=dict()
    if request.method=='POST':
        adminobj=Admindb()
        adminobj.firstname=request.POST.get('firstname')
        adminobj.lastname=request.POST.get('lastname')
        adminobj.username=request.POST.get('username')
        adminobj.email=request.POST.get('email')
        adminobj.password=request.POST.get('password')
        adminobj.confirmpassword=request.POST.get('confirmpassword')
        adminobj.save()
        print("eeeeerfrttyyyu")
        data['message']="registered sucessfully"
        data['error']=1
        return JsonResponse(data)



def admindel(request,dataid):
    datas=Admindb.objects.filter(id=dataid)
    datas.delete()
    return redirect(admintable)
def adminupdt(request,dataid):
    datas=Admindb.objects.filter(id=dataid)
    return render(request,"adminedit.html",{'datas':datas})

def updating(request,dataid):
    firstname=request.POST.get('firstname')
    lastname=request.POST.get('lastname')
    username=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('password')
    confirmpassword=request.POST.get('confirmpassword')
    Admindb.objects.filter(id=dataid).update(firstname=firstname,lastname=lastname,username=username,email=email,password=password,confirmpassword=confirmpassword)
    return redirect(admintable)
def prodlist(request):
    return render(request, 'prodlist.html')
