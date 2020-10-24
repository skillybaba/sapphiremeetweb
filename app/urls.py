from django.contrib import admin
from django.urls import path
from . import views
app_name='sapphiremeetapp'
urlpatterns = [
path('',views.home,name='home'),
path('about/',views.about,name='about'),
path('channel/',views.channelq,name='channel'),
path('enter/',views.enter,name='enter'),
path('notfound/',views.notfound,name='notfound'),
path('auth/',views.auth,name='auth'),
path('hostpage/<slug:docid>',views.hostpage,name='hostpage'),
path('entering/',views.entering,name='entering'),
path('contactus/',views.contact,name='contactus'),
path('price/',views.pricing,name='price'),
path('googleauth/',views.authA,name='authgoogle'),
path('appleauth/',views.authB,name='authapple'),
path('applesignup/',views.authC,name='authapplesignup'),

]
