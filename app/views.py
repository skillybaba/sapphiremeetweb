from django.shortcuts import render
from django import http
from . import models
def home(req):
    return render(req,'index-3.html')
def about(req):
    return http.HttpResponse('ok')
def contact(req):
    name=req.POST.get('name','')
    email=req.POST.get('email','')
    msg=req.POST.get('message','')
    subject=req.POST.get('subject','')
    arg={'val':False}
    if name!='' and email!='' and msg!='' and subject!='':
     val=models.msg()
     val.name=name
     val.email=email
     val.msg=msg
     val.subject=subject
     val.save()
     arg['val']=True

    return render(req,'contact.html',arg)
def pricing(req):
    return render(req,'pricing.html')
def channelq(req):
    print(req.POST.get('roomid'))
    return render(req,'channel.html',{'passcode':str(req.POST.get('passcode','')),"date":str(req.POST.get('date','random')),'topic':str(req.POST.get('top','random')),'roomid':str(req.POST.get('roomid','')),'name':str(req.POST.get('name',''))})
def enter(req):
    return render(req,'enter.html')
def notfound(req):
    return render(req,'notfound.html')
def auth(req):
    return render(req,'authpage.html')
def hostpage(req,docid):
    return render(req,'hostpage.html',{'docid':docid})
def authA(req,val):
    return render(req,'googleauth.html',{'val':val})
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
        arg['comeback']='true'
    arg['email']=email

    return render(req,'appleauth.html',arg)
def authC(req):
    username=req.POST.get('username','')
    email = req.POST.get('email','')
    password = req.POST.get('pass','')
    arg={}
    if username!="" and email !='' and password!='' and not models.user.objects.filter(email=email,passcode=password):
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
    return render(req,'chat.html')
def obs(req):
    return render(req,'index12.html')
def history(req):
    return render(req,'history.html')
def privacy(req):
    return render(req,'privacypolicy.html')
def tac(req):
    return render(req,'termandcondition.html')
def steps(req):
    return render(req,'steps.html')




