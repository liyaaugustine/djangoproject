from django.shortcuts import render
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
        uname=request.POST['uname']
        apass=request.POST['pass']
        admin=MyLogin(username=uname,password=apass)
        admin.save()
        return render(request,'login.html',{'message':'Succesfully Submitted'})
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
            sslc=request.POST['sslc']
            plus2=request.POST['plus2']
            degree=request.POST['degree']
            add=request.POST['additional']
            managment=Admission(email=mail,candidatename=cname,parentname=pname,phonenumber=num,category=categ,application=subject,sslc=sslc,plus2=plus2,degree=degree,qualification=add)
            managment.save()
            student=Admission.objects.get(email=mail,candidatename=cname,parentname=pname,phonenumber=num,category=categ,application=subject,sslc=sslc,plus2=plus2,degree=degree,qualification=add)
            request.session['id']=student.id
            return render(request,'admission.html',{'message':'Succesfully Submitted'})
            #return redirect('success')
        except:
            return render(request,'admission.html',{'message':'An Error Occured.Please Submitt again.'})
    admsn=Admission.objects.all()
    print(admsn)
    return render(request,'admission.html',{'adm':admsn})
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
def details(request):
    studdata=request.session['id']
    studdetails=Admission.objects.get(id=studdata)
    return render(request,'details.html',{'studentprofile':studdetails})
def success(request):
    sname=request.session['id']
    stud=Admission.objects.get(id=sname)
    return render(request,'sussess.html',{'children':stud})
def requests(request):
    req=request.session['id']
    reqdetail=Admission.objects.get(id=req)
    return render(request,'request.html',{'reqcheching':reqdetail})
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
