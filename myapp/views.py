from django.shortcuts import render
from django.http import HttpResponse    

# Create your views here.
def index(request):
    return  HttpResponse('hai hellow')
def home(req):
    return HttpResponse('Good Morning')    
def first(request):
    return render(request,'first.html')