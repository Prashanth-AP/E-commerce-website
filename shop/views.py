from django.shortcuts import render
from .models import Product

# Create your views here.
from django.http import HttpResponse
from math import ceil

#create the function
def index(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"shop/index.html", params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return render(request,'shop/contact.html')

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request, myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, "shop/productView.html",{'product':product[0]})

def checkout(request):
    return HttpResponse("We are at checkout")


