from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse  
from . models import *
from django.core.mail import send_mail

# Create your views here.
def new(r):
    return HttpResponse('Hai Its a new beginning!!')
def home(request):
    return render(request,'welcomepage.html')
def upcount(request):
    newdata=request.session['aid']
    if request.method=='POST':
        snum=request.POST['stud']
        cnum=request.POST['crse']
        tnum=request.POST['tchr']
        total=Count.objects.filter(loginid=newdata)
        if total:
            Count.objects.filter(loginid=newdata).update(student=snum,course=cnum,teacher=tnum)
            return render(request,'welcomepage.html')
        else:
            details=Count(student=snum,course=cnum,teacher=tnum,loginid_id=newdata)
            details.save()  
            return render(request,'welcomepage.html')
    else:
        return render(request,'welcomepage.html')
def displaycount(request):
    datas=Count.objects.all()
    clg=[{'cstud':itm.student,'csub':itm.course,'ctchr':itm.teacher}for itm in datas]
    return JsonResponse({'mydata':clg})

def contact(request):
    if request.method=='POST':
        try:
            sname=request.POST['name']
            mail=request.POST['mail']
            number=request.POST['num']
            mesg=request.POST['msg']
            quest=Message(studentname=sname,mail=mail,contact=number,message=mesg,status='active')
            quest.save()
            return render(request,'contact.html',{'msg':'Message sended'})
        except Exception as error:
            return render(request,'contact.html',{'msg':error})
    return render(request,'contact.html')
def editcontact(request):
    newdata=request.session['aid']
    if request.method=='POST':
        adres=request.POST['addrs']
        mail=request.POST['mail']
        fnum=request.POST['num1']
        snum=request.POST['num2']
        cdata=ContactDetails.objects.filter(loginid=newdata)
        if cdata:
            ContactDetails.objects.filter(loginid=newdata).update( address=adres,email=mail,firstnum=fnum,secnum=snum)
            return render(request,'contact.html')
        else:
            cont=ContactDetails(address=adres,email=mail,firstnum=fnum,secnum=snum,loginid_id=newdata)
            cont.save()
            return render(request,'contact.html')
    else:
        return render(request,'contact.html')
def showcontact(request):
    newinfo=ContactDetails.objects.all()
    datas=[{'info':item.address,'cmail':item.email,'ofice':item.firstnum,'direct':item.secnum}for item in newinfo ]
    return JsonResponse({'mydata':datas})
def messages(request): #students sending doubts
    actmsg=Message.objects.filter(status='active')
    inact=Message.objects.filter(status='inactive')
    return render(request,'messags.html',{'instatus':inact,'astatus':actmsg})
def replymsg(request,rplid):
    newdata=request.session['aid']
    forid=Message.objects.get(id=rplid)
    if request.method=='POST':
        try:
            rmsg=request.POST['reply']
            foremailmsg=Reply.objects.filter(mesageid=rplid)
            if foremailmsg:
                foremail=Reply.objects.filter(mesageid=rplid).update(reply=rmsg)
                Message.objects.filter(id=rplid).update(status='inactive')
                foremail=Reply.objects.get(mesageid=rplid)
                send_mail(
                    'Reply From St Thomas College,',
                    foremail.reply,
                    'liyaaugustinek@gmail.com',
                    [forid.mail],
                    fail_silently=False,
                    )
                return render(request,'reply.html',{'msg':'Message Sended','question':forid})
            else:
                messge=Reply(reply=rmsg,loginid_id=newdata,mesageid_id=rplid)
                messge.save()
                Message.objects.filter(id=rplid).update(status='inactive')
                send_mail(
                    'Reply From St Thomas College,',
                    messge.reply,
                    'liyaaugustinek@gmail.com',
                    [forid.mail],
                    fail_silently=False,
                    )
                return render(request,'reply.html',{'msg':'Message Sended','question':forid}) 
        except Exception as err:
            return render(request,'reply.html',{'msg':err})
    return render(request,'reply.html',{'question':forid})    
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
def upmonth(request):
    newdata=request.session['aid']
    if request.method=='POST':
        mnth=request.POST['month']
        mnt=Month.objects.filter(loginid=newdata)
        if mnt:
            Month.objects.filter(loginid=newdata).update(month=mnth)
            return redirect('about')
        else:
            newmonth=Month(month=mnth,loginid_id=newdata)
            newmonth.save()
            return redirect('about')
    else:
        newevnt=Event.objects.all()
        return render(request,'about.html',{'evnt':newevnt,})
def showmonth(request):
    newmnth=Month.objects.all()
    months=[{'mymonth':item.month} for item in newmnth]
    return JsonResponse({'mydata':months})

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
        except:
            return render(request,'studlogin.html',{'msg':'Invalid Userdetails'})
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
    studdata=Admission.objects.get(id=reqid)#admin viewing single pg student  profile
    return render(request,'details.html',{'studentprofile':studdata})
def apgmail(request,apid): #sending accept message mail to PG
    foremail=Admission.objects.get(id=apid)
    send_mail(
        'Congrats,',
        'your application for PG Course in St.Thomas is Accepted.For more details please contact us soon!',
        'liyaaugustinek@gmail.com',
        [foremail.email],
        fail_silently=False,
    )
    return render(request,'details.html',{'studentprofile':foremail,'msg':'Accepted mail sended to student'})
def rpgmail(request,rpid): #sending Reject message mail to PG
    foremail=Admission.objects.get(id=rpid)
    send_mail(
        'Sorry!!!',
        'Your Application for PG Course in St.Thomas is Rejectd',
        'liyaaugustinek@gmail.com',
        [foremail.email],
        fail_silently=False,
    )
    return render(request,'details.html',{'studentprofile':foremail,'msg':'Rejectdion  mail sended to student'})
def ugdetails(request,ugid):#admin viewing single ug student  profile
    ugdata=Degree.objects.get(id=ugid)
    return render(request,'ugdetails.html',{'ugstud':ugdata})
def augmail(request,amid): #sending accept message mail to UG
    foremail=Degree.objects.get(id=amid)

    send_mail(
        'Congrats!!!,',
        'Your application for UG Course in St.Thomas is Accepted.For more details please contact us soon!',
        'liyaaugustinek@gmail.com',
        [foremail.email],
        fail_silently=False,
        )
    return render(request,'ugdetails.html',{'ugstud':foremail,'msg':'Accepted mail sended to student'})
def rugmail(request,rmid): #sending Reject message mail to UG
    foremail=Degree.objects.get(id=rmid)

    send_mail(
        'Sorry',
        'Your Application for UG Course in St.Thomas is Rejectd',
        'liyaaugustinek@gmail.com',
        [foremail.email],
        fail_silently=False,
    )
    return render(request,'ugdetails.html',{'ugstud':foremail,'msg':'Rejectdion  mail sended to student'})
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
    if request.method=='POST':
        searchword=request.POST['srch']
        searchstud=Admission.objects.filter(Q(email__icontains=searchword) | Q(candidatename__icontains=searchword) | 
        Q(parentname__icontains=searchword))
        return render(request,'request.html',{'reqchekhing':searchstud})
    req=Admission.objects.all()
    return render(request,'request.html',{'reqchekhing':req})
def ugreq(request):#ug students requests
    if request.method=='POST':
        searchword=request.POST['srch']
        searchstud=Degree.objects.filter(Q(email__icontains=searchword) | Q(candidatename__icontains=searchword) | 
        Q(parentname__icontains=searchword))
        return render(request,'ugreq.html',{'ugcheck':searchstud})
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
        if 'sslc' in request.FILES:
            slc=request.FILES['sslc']
        else:
            slc=request.POST['sslc']    
        if 'plus' in request.FILES:
            plus2=request.FILES['plus']
        else:
            plus2=request.POST['plus']
        if 'degre' in request.FILES:
            degree=request.FILES['degre']
        else:
            degree=request.POST['degre']
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
        if 'sslc' in request.FILES:
            slc=request.FILES['sslc']
        else:
            slc=request.POST['sslc']
        if 'plus' in request.FILES:
            plus2=request.FILES['plus']
        else:
            plus2=request.POST['plus']
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
def delevent(request,evtid):#for deleting an event
    Event.objects.get(id=evtid).delete()
    return redirect('about')
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
            day=request.POST['day']
            evnt=request.POST['event']
            evnts=Event(day=day,event=evnt,loginid_id=admin)
            evnts.save()
            return render(request,'editing.html',{'mesg':'Succes'})
        except Exception as error:
            return render(request,'editing.html',{'mesg':error})
    return render(request,'editing.html')

def studentwelcome(request):
    swelcome=request.session['sid']
    
    return render(request,'studentwelcome.html',{'stwelcome':swelcome})
def addedimage(request):
    pics=Image.objects.all()
    return render(request,'addedimage.html',{'allimg':pics})
def delimage(request,pcid):
    Image.objects.filter(id=pcid).delete()
    return redirect('addedimage')
def ugacademic(request): #displaying ug details 
    alldata=UgAcademics.objects.all()
    return render(request,'ugacademic.html',{'uginfo':alldata})
def pgacademic(request): #displaying pg details
    alldata=PgAcademics.objects.all()
    return render(request,'pgacademic.html',{'pginfo':alldata})
def ugfees(request): #adding ug details
    newdata=request.session['aid']
    if request.method=='POST':
        try:
            usub=request.POST['ucrse']
            umoney=request.POST['ufees']
            uqual=request.POST['ueligibility']
            ujobs=request.POST['ujob']
            ugacd=UgAcademics(subjects=usub,fees=umoney,eligibility=uqual,job=ujobs,loginid_id=newdata)
            ugacd.save()
            return render(request,'ugfees.html',{'msg':'Succesfully added'})
        except Exception as error:
            return render(request,'ugfees.html',{'msg':error})
    return render(request,'ugfees.html')
def pgfees(request): #adding pg details
    newdata=request.session['aid']
    if request.method=='POST':
        try:
            psub=request.POST['pcrse']
            pmoney=request.POST['pfees']
            pqual=request.POST['peligibility']
            pjobs=request.POST['pjob']
            pgacd=PgAcademics(subjects=psub,fees=pmoney,eligibility=pqual,job=pjobs,loginid_id=newdata)
            pgacd.save()
            return render(request,'pgfees.html',{'msg':'Succesfully added'})
        except Exception as error:
            return render(request,'pgfees.html',{'msg':error})
    return render(request,'pgfees.html')
def delugfees(request,ufid):
    UgAcademics.objects.filter(id=ufid).delete()
    return redirect('ugacademic')
def delpgfees(request,pfid):
    PgAcademics.objects.filter(id=pfid).delete()
    return redirect('pgacademic')
def editugfees(request,eufid):
    oldug=UgAcademics.objects.get(id=eufid)
    if request.method=='POST':
        usubj=request.POST['subj']
        ufee=request.POST['fee']
        uelig=request.POST['qual']
        ujob=request.POST['pjob'] 
        newug=UgAcademics.objects.filter(id=eufid).update(subjects=usubj,fees=ufee,eligibility=uelig,job=ujob)
        return render(request,'editugfees.html',{'pginfo':newug})
    return render(request,'editugfees.html',{'pginfo':oldug})
     
def editpgfees(request,epfid):
    oldpg=PgAcademics.objects.get(id=epfid)
    if request.method=='POST':
        psubj=request.POST['subj']
        pfee=request.POST['fee']
        pelig=request.POST['qual']
        pjob=request.POST['pjob']
        newpg=PgAcademics.objects.filter(id=epfid).update(subjects=psubj,fees=pfee,eligibility=pelig,job=pjob)
        return render(request,'editpgfees.html',{'pginfo':newpg,'msg':'Updated Succesfully'})
    return render(request,'editpgfees.html',{'pginfo':oldpg})



