from django.shortcuts import render
from django import http

def home(req):
    return render(req,'index-3.html')
def about(req):
    return http.HttpResponse('ok')
def contact(req):
    return http.HttpResponse('ok')
def pricing(req):
    return http.HttpResponse('ok')
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