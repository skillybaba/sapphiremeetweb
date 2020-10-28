from django.shortcuts import render
from django import http
from . import models
def home(req):
    return render(req,'index-3.html')
def about(req):
    return http.HttpResponse('ok')
def contact(req):
    return render(req,'contact.html')
def pricing(req):
    return render(req,'pricing.html')
def channelq(req):
    print(req.POST.get('roomid'))
    return render(req,'channel.html',{'roomid':str(req.POST.get('roomid','')),'name':str(req.POST.get('name',''))})
def enter(req):
    return render(req,'enter.html')
def notfound(req):
    return render(req,'notfound.html')
def auth(req):
    return render(req,'authpage.html')
def hostpage(req,docid):
    return render(req,'hostpage.html',{'docid':docid})
def authA(req):
    return render(req,'googleauth.html')
def entering(req):
    return render(req,'index.html')
def authB(req):
    email = req.POST.get('email','')
    password = req.POST.get('password','')
    arg={}
    if email!='' and password!='' and models.user.objects.filter(email=email,passcode=password):
        arg['auth']='true'
    else :
        arg['auth']='false'
    return render(req,'appleauth.html',arg)
def authC(req):
    username=req.POST.get('username','')
    email = req.POST.get('email','')
    password = req.POST.get('pass','')
    arg={}
    if username!="" and email !='' and password!='' and not models.user.objects.filter(email=email,name=username,passcode=password):
        a=models.user()
        a.email=email
        a.name=username
        a.passcode=password
        a.save()
        arg['auth']=True
    elif email=='' and password=='' and username=='':
        arg['auth']='fs'
    else:
        arg['auth']=False
    
    return render(req,'applesignup.html',arg)
def commingsoon(req):
    return render(req,'coomingsoon.html')
def obs(req):
    return render(req,'index12.html')