from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer

# Create your views here.
def index(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name','')
        product_id=request.POST.get('product_id','')
        Product_quantity=request.POST.get('Product_quantity','')
        Description=request.POST.get('Description','')
        print(name,product_id,Product_quantity,Description)
        customer=Customer(name=name,description=Description,product_quantity=Product_quantity,product_id=product_id)
        customer.save()
    return render(request,'customer/customer.html')

def home(request):
    return render(request,'customer/home.html')