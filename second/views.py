from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse  
from . models import *

# Create your views here.
def new(r):
    return HttpResponse('Hai Its a new beginning!!')
def home(request):
    teachr=Count.objects.get(id=1)
    return render(request,'welcomepage.html',{'stud':teachr})

def contact(request):
    if request.method=='POST':
        try:
            sname=request.POST['name']
            mail=request.POST['mail']
            number=request.POST['num']
            mesg=request.POST['msg']
            quest=Message(studentname=sname,mail=mail,contact=number,message=mesg)
            quest.save()
            return render(request,'contact.html',{'msg':'Message sended'})
        except Exception as error:
            return render(request,'contact.html',{'msg':error})
    info=ContactDetails.objects.get(id=1)
    return render(request,'contact.html',{'details':info})

def messages(request): #students sending doubts
    msg=Message.objects.all()
    return render(request,'messags.html',{'messg':msg})
def img(request):
    pic=Image.objects.all()       
    return render(request,'images.html',{'mesg':pic})
def images(request):#admin adding new image.
    admin=request.session['aid']
    if request.method=='POST':
        try:
            imag=request.FILES['img']
            photo=Image(images=imag,loginid_id=admin)
            photo.save()
            pic=Image.objects.all()   
            return render(request,'images.html',{'mesg':pic})
        except Exception as error:
            return render(request,'images.html',{'messg':error})
    else:
        pic=Image.objects.all()       
        return render(request,'images.html',{'mesg':pic})
def about(request):
    newevnt=Event.objects.all()
    return render(request,'about.html',{'evnt':newevnt})
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
            uname=request.POST['uname']#liya@gmail.com
            apass=request.POST['pass']#llllll
            admin=MyLogin.objects.get(username=uname,password=apass)
            #admin=MyLogin(username=uname,password='pass') username and pswrd for admin inserted and set through sql.
            #admin.save()
            request.session['aid']=admin.id
            return redirect('admin')
        except Exception as err:
            return render(request,'login.html',{'message':err })
    return render(request,'login.html')
def alogout(request):
    del request.session['aid']
    return redirect('home')
def studlogin(request): # student logging
    if request.method=='POST':
        try:
            usname=request.POST['uname']
            pswrd=request.POST['pass']
            stud=StudentLogin.objects.get(username=usname,password=pswrd)
            request.session['sid']=stud.id
            print('---------------------------------------------------------------------')
            return redirect('studentwelcome')
        except Exception as err:
            return render(request,'studlogin.html',{'msg':err})
    return render(request,'studlogin.html')
def studlogout(request):#student logout
    del request.session['sid']
    return redirect('home')

def admission(request):
    if request.method=='POST':
        try:
            usertype=request.POST['usertype']
            mail=request.POST['mail']
            cname=request.POST['candidate']
            pname=request.POST['parent']
            num=request.POST['contact']
            categ=request.POST['category']
            smark=request.POST['sslcmark']
            pmark=request.POST['plusmark'] 
            sslc=request.FILES['sslc']
            plus2=request.FILES['plus2'] 
            add=request.POST['additional']
            pswrd=request.POST['pass']

            log=StudentLogin(password=pswrd,username=mail)
            log.save()
            request.session['sid']=log.id
            if usertype=='ug':
                subject=request.POST['sub']
                dgr=Degree(usertype=usertype,email=mail,candidatename=cname,parentname=pname,phonenumber=num,category=categ,
                application=subject,sslcmark=smark,plus2mark=pmark,sslc=sslc,plus2=plus2,qualification=add,logid=log)
                dgr.save()
                
                return redirect('ugsuccess')
            else:
                subject=request.POST['subj']
                dmark=request.POST['degremark']
                mdegree=request.FILES['degree']
                managment=Admission(usertype=usertype,email=mail,candidatename=cname,parentname=pname,phonenumber=num,category=categ,
                application=subject,sslcmark=smark,plus2mark=pmark,ugmark=dmark,sslc=sslc,plus2=plus2,degree=mdegree,
                qualification=add,logid=log)
                managment.save()
                
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
    studdata=Admission.objects.get(id=reqid)#admin viewing pg students  profile
    return render(request,'details.html',{'studentprofile':studdata})
def ugdetails(request,ugid):#admin viewing ug students  profile
    ugdata=Degree.objects.get(id=ugid)
    return render(request,'ugdetails.html',{'ugstud':ugdata})
def delete(request,delid):#admin deleting from pg requests
    Admission.objects.filter(id=delid).delete()
    return redirect('requests')
def ugdel(request,udid):#admin deleting from ug requests
    Degree.objects.filter(id=udid).delete()
    return redirect('ugreq')
def success(request):#welcome page for pg
    return render(request,'sussess.html')
def ugsuccess(request):#welcome page for ug
    return render(request,'ugsuccess.html')
def requests(request):#pg students requests
    req=Admission.objects.all()
    return render(request,'request.html',{'reqchekhing':req})
def ugreq(request):#ug students requests
    degre=Degree.objects.all()
    return render(request,'ugreq.html',{'ugcheck':degre})
def sdetails(request):
    child=request.session['sid']#pg student viewing profile
    childinfo=Admission.objects.get(logid=child)
    print('-----------------------------------------------------')
    return render(request,'singleview.html',{'childdata':childinfo})
def ugstudprofile(request):#ug student viewing profile
    child=request.session['sid']
    ugdetails=Degree.objects.get(logid=child)
    return render(request,'ugstudprofile.html',{'ugdata':ugdetails})
def upadmission(request): #updating pg student themselves
    updating=request.session['sid']
    if request.method=='POST':
        print('checking my updation--------------------------------------------------------')
        mail=request.POST['mail']
        cname=request.POST['cname']
        pname=request.POST['pname']
        num=request.POST['phone']
        categ=request.POST['ctgry']
        subject=request.POST['sub']
        slcmark=request.POST['ssperc']
        plmark=request.POST['plperc']
        dgmark=request.POST['degperc']
        slc=request.FILES['sslc']#error in these three  file fields
        plus2=request.FILES['plus']
        degree=request.FILES['degre']
        add=request.POST['add']
        Admission.objects.filter(logid=updating).update(email=mail,candidatename=cname,parentname=pname,
        phonenumber=num,category=categ,application=subject,sslcmark=slcmark,plus2mark=plmark,
        ugmark=dgmark,sslc=slc,plus2=plus2,degree=degree,qualification=add)

        studdata=Admission.objects.get(logid=updating)
        return render(request,'singleview.html', {'childdata':studdata})  
    else:
        studdata=Admission.objects.get(logid=updating)
        return render(request,'singleview.html', {'childdata':studdata})  
def updateug(request):  #updating ug student themselves
    updating=request.session['sid']
    if request.method=='POST':
        mail=request.POST['mail']
        cname=request.POST['cname']
        pname=request.POST['pname']
        num=request.POST['phone']
        categ=request.POST['ctgry']
        subject=request.POST['sub']
        slcmark=request.POST['ssperc']
        plmark=request.POST['plperc']
        slc=request.FILES['sslc']# also error in these two file fields
        plus2=request.FILES['plus']
        add=request.POST['add']
        print(slc)
        Degree.objects.filter(logid=updating).update(email=mail,candidatename=cname,parentname=pname,
        phonenumber=num,category=categ,application=subject,sslcmark=slcmark,plus2mark=plmark,
        sslc=slc,plus2=plus2,qualification=add)
        student=Degree.objects.get(logid=updating)
        return render(request,'ugstudprofile.html',{'ugdata':student})
    else:
        student=Degree.objects.get(logid=updating)
        return render(request,'ugstudprofile.html',{'ugdata':student})
def delevent(request):
    pass#for deleting an event  
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
    adm=request.session['aid']
    return render(request,'admin.html',{'logging':adm})
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
def viewfile(request,vid):
    vimg=Admission.objects.get(id=vid)
    return render(request,'viewfile.html',{'display':vimg})
def plustwo(request,plid):
    vimg=Admission.objects.get(id=plid)
    return render(request,'plustwo.html',{'display':vimg})
def degree(request,dgid):
    vimg=Admission.objects.get(id=dgid)
    return render(request,'degree.html',{'display':vimg})
def ugsslc(request,sscid):
    dimg=Degree.objects.get(id=sscid)
    return render(request,'ugsslc.html',{'degre':dimg})
def ugplustwo(request,upid):
    dimg=Degree.objects.get(id=upid)
    return render(request,'ugplustwo.html',{'degre':dimg})
def editing(request):
    admin=request.session['aid']
    if request.method=='POST':
        try:
            mnth=request.POST['month']
            day=request.POST['day']
            evnt=request.POST['event']
            evnts=Event(month=mnth,day=day,event=evnt,loginid_id=admin)
            evnts.save()
            return render(request,'editing.html',{'mesg':'Succes'})
        except Exception as error:
            return render(request,'editing.html',{'mesg':error})
    return render(request,'editing.html')
def addcontact(request):
    admin=request.session['aid']
    if request.method=='POST':
        try:
            adrs=request.POST['addrs']
            mail=request.POST['mail']
            office=request.POST['office']
            direct=request.POST['director']
            cont=ContactDetails(address=adrs,email=mail,firstnum=office,secnum=direct,loginid_id=admin)
            cont.save()
            return render(request,'addcontact.html',{'mesg':'Success'})
        except Exception as error:
            return render(request,'addcontact.html',{'mesg':error})
    return render(request,'addcontact.html')
def addteacher(request):
    admin=request.session['aid']
    if request.method=='POST':
        try:
            child=request.POST['stud']
            teach=request.POST['teacher']
            course=request.POST['course']
            teachr=Count(student=child,teacher=teach,course=course,loginid_id=admin)
            teachr.save()
            return render(request,'teachers.html',{'mesg':'Succesful'})
        except Exception as error:
            return render(request,'teachers.html',{'mesg':error})
    return render(request,'teachers.html')
def studentwelcome(request):
    return render(request,'studentwelcome.html')

