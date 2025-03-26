from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

#create the function
def index(request):
    return render(request,'blog/index.html')
