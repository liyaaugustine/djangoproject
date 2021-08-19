from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse  
from . models import *  

# Create your views here.
def index(request):
    return  HttpResponse('hai hellow')
def home(req):
    return HttpResponse('Good Morning')    
def first(request):
    return render(request,'first.html')
def facebook(request):
    return render(request,'facebook.html')
def calculater(request):
    return render(request,'mycalculater.html')
def form(request):
    return render(request,'forms.html')
def add(request):
    return render(request,'add.html')
def result(request):
    if request.method=='POST':     
        first=request.POST['fnum']
        sec=request.POST['snum']
        sum=int(first)+int(sec)
        print(sum)
        return render(request,'add.html',{'answer':sum})
    return render(request, 'add.html')
def ajaxadd(request):
    return render(request,'ajax.html')
def ajaxsum(request):
    fir=request.POST['firstnum']
    sec=request.POST['secondnum']
    sum=int(fir)+int(sec)
    print(fir)
    print(sum)
    return JsonResponse({
        'result':sum
    })
def parent(request):
    return render(request,'parent.html')
def child(request):
    if request.method=='POST':
        try:
            tit=request.POST['head']
            pub=request.POST['publi']
            artobj=Article(headline=tit,publications=pub)
            artobj.save()
            return render(request,'child.html', {'message':'succesfully'})
        except Exception as error:
            return render(request,'child.html', {'message':error})
    articles=Article.objects.all() 
    print(articles)
    return render(request,'child.html',{'artcle':articles})
def uparticle(request,itmid):
    allpub=Article.objects.get(id=itmid)
    return render(request,'updatearticle.html',{'pub':allpub})
    if request.method=='POST':
        try:
            heading=request.POST['hline']
            publication=request.POST['public']
            upvalue=Article.objects.filter(id=itmid).update(headline=heading, publications=publication)
            print(upvalue)
            return render(request,'updatearticle.html', {'msg': 'updated'})
        except Exception as error: 
            return render(request,'updatearticle.html', {'msg': error})  
    #return render(request,'updatearticle.html')    
def foreign(request):
    if request.method=='POST':
        try:
            uname=request.POST['uname']
            passw=request.POST['psw']
            fname=request.POST['fname']
            lname=request.POST['lname']   
            date=request.POST['dte']
            place=request.POST['place']
            pname=request.POST['pname']
            mobile=request.POST['mble']
            details=Login(Username=uname,Password=passw)
            details.save()
            if request.FILES['pic']:
                pics=request.FILES['pic']
                print(pics,'------------------')
                pictures=Profilepic(profilepic=pics,loginid=details)
                pictures.save()
            
            details2=UserDetails(firstname=fname,lastname=lname,date=date,place=place,parentname=pname,phone=mobile,loginid=details)
            details2.save()
        
            request.session['id']=details.id
            #return render(request,'foreign.html',{'message':'succesfully'})
            return redirect('home2')
        except Exception as error:
             return render(request,'foreign.html',{'message':error})
    creq=UserDetails.objects.all()
    return render(request,'foreign.html',{'chreq':creq})
def sampleform(request):
    print("Checking")
    new=request.GET['uname']
    ucheck=Login.objects.filter(Username=new).exists()
    print(ucheck)
    if ucheck :
        return JsonResponse({
            'msg':True
        })
    else:
        return JsonResponse({
            'msg':False
        })
def logauth(request):
    if request.method=='POST':
        try:
            uname=request.POST['uname']
            passw=request.POST['psw']
            ulog=Login.objects.get(Username=uname,Password=passw)
            request.session['id']=ulog.id#session is a memmory for storing value and it is like global.
            #request.session['name']=ulog.Username
            #print(request.session['name'])
            return redirect('home2')
        except:
            return render(request,'logauth.html',{'mesge':'Invalid Userdetails'})
            #return render(request,'logauth.html',{'mesge':error})
    return render(request,'logauth.html')
def home2(request):
    try:
        logid=request.session['id']
        udetail=UserDetails.objects.get(loginid=logid)
        #print(udetail.firstname)
        #print(logid)
        return render(request,'home.html',{'userd':udetail})
    except Exception as error:
         return render(request,'home.html',{'err':error})
def signout(request):
    del request.session['id']
    return redirect('logauth')
def vprofile(request):
    prodata=request.session['id']
    prodetails=UserDetails.objects.get(loginid=prodata)
    logindata=Login.objects.get(id=prodata)
    return render(request,'profile.html',{'profile':prodetails, 'logdata':logindata})
def checking(request):
    checkdet=UserDetails.objects.all()
    return render(request,'checking.html',{'checkdetails':checkdet})
def uprofile(request):
    if request.method=='POST':
        print('work')
        fname=request.POST['fname']
        lname=request.POST['lname']   
        date=request.POST['ndate']
        place=request.POST['place']
        pname=request.POST['pname']
        mobile=request.POST['phone']
        id=request.session['id']
        UserDetails.objects.filter(loginid=id).update(firstname=fname,lastname=lname,date=date,place=place,parentname=pname,
        phone=mobile)
        usrdata=UserDetails.objects.get(id=userid)
        return render(request,'vsingle.html',{'profile':usrdata})
        #return redirect('vsingle')
    return render(request,'vsingle.html')
def vsingle(request,userid):
    if request.method=='POST':
        print('working -------------------------------------------------------------------------------------')
        fname=request.POST['fname']
        lname=request.POST['lname']   
        date=request.POST['ndate']
        place=request.POST['place']
        pname=request.POST['pname']
        mobile=request.POST['phone']
        print(type(date))
        #id=request.session['id']
        UserDetails.objects.filter(id=userid).update(firstname=fname,lastname=lname,date=date,place=place,parentname=pname,
        phone=mobile)
        usrdata=UserDetails.objects.get(id=userid)
        return render(request,'vsingle.html',{'profile':usrdata})
    else:
        usrdata=UserDetails.objects.get(id=userid)
        return render(request,'vsingle.html',{'profile':usrdata})
def delete(request,delid): #admin deleting
    logdta=UserDetails.objects.get(id=delid)
    logid=logdta.loginid_id
    print(logid)
    dellog=Login.objects.filter(id=logid).delete()
    deluser=UserDetails.objects.filter(id=delid).delete()
    
    return redirect('foreign')
def deleteacc(request):
    acc=request.session['id']
    UserDetails.objects.filter(loginid=acc).delete()
    Login.objects.filter(id=acc).delete()
    return redirect('foreign')



