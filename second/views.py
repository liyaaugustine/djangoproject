from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse  
from . models import *

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
def achevments(request):
    return render(request,'achevments.html')
def milestones(request):
    return render(request,'milestones.html')
def activity(request):
    return render(request,'activity.html')
def socialwork(request):
    return render(request,'socialwork.html')
def msw(request):
    return render(request,'msw.html')
def bsw(request):
    return render(request,'bsw.html')
def bswsyllabus(request):
    return render(request,'bswsyllabus.html')
def mswsyllabus(request):
    return render(request,'mswsyllabus.html')
def login(request):
    if request.method=='POST':
        try:
            uname=request.POST['uname']
            apass=request.POST['pass']
            admin=MyLogin(username='liya@gmail.com',password='123456')
            admin.save()
            
            adlog=MyLogin.objects.get(username=uname,password=apass)#  error,this 2 line for setting default uname and passwd
            request.session['uname']=adlog.username
            
            #return render(request,'login.html',{'message':'Success'})
            return redirect('admin')
        except Exception as err:
            return render(request,'login.html',{'message':err })
    return render(request,'login.html')
def admission(request):
    if request.method=='POST':
        try:
            mail=request.POST['mail']
            cname=request.POST['candidate']
            pname=request.POST['parent']
            num=request.POST['contact']
            categ=request.POST['category']
            subject=request.POST['sub']
            sslc=request.FILES['sslc']
            plus2=request.FILES['plus2']
            degree=request.FILES['degree']
            add=request.POST['additional']
            managment=Admission(email=mail,candidatename=cname,parentname=pname,phonenumber=num,category=categ,application=subject,sslc=sslc,plus2=plus2,degree=degree,qualification=add)
            managment.save()
            info=Admission.objects.get(email=mail)
            request.session['id']=info.id
            #return render(request,'admission.html',{'message':'Succesfully Submitted'})
            return redirect('success')
        except Exception as error:
            return render(request,'admission.html',{'message':error})
    return render(request,'admission.html')
def admson(request):
    adm=request.GET['email']
    echeck=Admission.objects.filter(email=adm).exists()
    print(echeck)
    if echeck:
        return JsonResponse({
            'mesg':True
        })
    else:
        return JsonResponse({
            'mesg':False
        })
def details(request,reqid):
    studdata=Admission.objects.get(id=reqid)#admin viewing profile
    return render(request,'details.html',{'studentprofile':studdata})
def delete(request,delid):
    Admission.objects.filter(id=delid).delete()
    return redirect('requests')
def success(request):
    return render(request,'sussess.html')
def requests(request):
    req=Admission.objects.all()
    return render(request,'request.html',{'reqchekhing':req})
def sdetails(request):
    child=request.session['id']#student viewing profile
    childinfo=Admission.objects.get(id=child)
    return render(request,'singleview.html',{'childdata':childinfo})
def computerscience(request):
    return render(request,'computerscience.html')
def bsccs(request):
    return render(request,'bscCS.html')
def cssyllabus(request):
    return render(request,'cssyllabus.html')
def library(request):
    return render(request,'library.html')
def hostel(request):
    return render(request,'hostel.html')
def computerlab(request):
    return render(request,'computerlab.html')
def english(request):
    return render(request,'english.html')
def baenglish(request):
    return render(request,'BA.html')
def maenglish(request):
    return render(request,'MA.html')
def admin(request):
    return render(request,'admin.html')
def psychology(request):
    return render(request,'psychology.html')
def msc(request):
    return render(request,'msc.html')
def bsc(request):
    return render(request,'bsc.html')
def bscsyllabus(request):
    return render(request,'bscsyllabus.html') 
def mscsyllabus(request):
    return render(request,'mscsyllabus.html') 
def title(request):
    if request.method=='POST':
        tit=request.POST['title']
        print(tit)#print in cmd 
        head=Publication(title=tit)#inserting value
        head.save()
        return render(request,'article.html',{'message':'Succesful'})
    return render(request,'article.html')
