from django.shortcuts import render
from django import http

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
    return render(req,'appleauth.html')
def authC(req):
    return render(req,'applesignup.html')
def commingsoon(req):
    return render(req,'coomingsoon.html')
def obs(req):
    return render(req,'index12.html')