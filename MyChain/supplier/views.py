from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Supplied_list,Requiredlist
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name','')
        product_id=request.POST.get('product_id','')
        product_quantity=request.POST.get('Product_quantity','')
        Description=request.POST.get('Description','')
        supplied_list=Supplied_list(name=Supplier_name,product_id=product_id,product_quantity=product_quantity,description=Description)
        supplied_list.save()
    return render(request,'supplier/supplier.html')
    # data=Requiredlist.objects.all()
    # lst= {
    #         "rcrd_list":data
    #     }
    # return render(request,'supplier/supplier.html')

def u_login(request):
    context={}
    lst={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username, password=password)
        if user==None:
            context["error"]="innvalid "
            return render(request,"supplier/login.html",context)
        if user.is_authenticated:
            username=user.username
            data=Requiredlist.objects.filter(supplier_name=username)
            lst={"rcrd_list":data,'suppliername':username}
            # print(data.product_quantity)
            login(request, user)
            # return HttpResponseRedirect(reverse('index'),lst)
            return render(request,'supplier/supplier.html',lst)
        
    else:
        return render(request, "supplier/login.html", context)
    