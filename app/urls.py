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
path('commingsoon/',views.commingsoon,name='comming'),
path('obs/',views.obs,name='OBS'),
path('history/',views.history,name='history'),
path('termsandcondition/',views.tac,name='tac'),
path('privacypolicy/',views.privacy,name='privacy'),
path('steps/',views.steps,name='steps'),

]
