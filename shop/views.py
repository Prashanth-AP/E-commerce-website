from django.shortcuts import render
from .models import Product

# Create your views here.
from django.http import HttpResponse
from math import ceil

#create the function
def index(request):
    product=Product.objects.all()
    print(product)
    n=len(product)
    no_of_slides=n//4+ceil((n/4)-(n//4))
    # params={'no_of_slides':no_of_slides,'range':range(1,no_of_slides),'product':product,}
    allProds = [[product, range(1, no_of_slides), no_of_slides], [product, range(1, no_of_slides), no_of_slides]]
    params = {'allProds': allProds}
    return  render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")


