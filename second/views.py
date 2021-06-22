from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def new(r):
    return HttpResponse('Hai Its a new beginning!!')
def home(request):
    return render(request,'welcomepage.html')
def contact(request):
    return render(request,'contact.html')
def images(request):
    return render(request,'images.html')
def about(request):
    return render(request,'about.html')