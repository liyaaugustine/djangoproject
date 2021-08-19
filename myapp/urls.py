
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('home', views.home),
    path('first',views.first, name='first'),
    path('facebook',views.facebook, name='facebook'),
    path('calculater',views.calculater, name='calculater'),
    path('form', views.form, name='form'),
    path('add', views.add, name='add'),
    path('result', views.result, name='result'),
    path('ajaxadd', views.ajaxadd, name='ajaxadd'),
    path('ajaxsum', views.ajaxsum, name='ajaxsum'),
    path('parent',views.parent,name='parent'),
    path('child',views.child,name='child'),
    path('foreign',views.foreign,name='foreign'),
    path('sampleform',views.sampleform,name='sampleform'),
    path('logauth',views.logauth,name='logauth'),
    path('home2',views.home2,name='home2'),
    path('signout',views.signout,name='signout'),
    path('vprofile',views.vprofile,name='vprofile'),
    path('checking',views.checking,name='checking'),
    path('uprofile',views.uprofile,name='uprofile'),
    path('vsingle/<int:userid>',views.vsingle,name='vsingle'),
    path('delete/<int:delid>',views.delete,name='delete'),
    path('deleteacc',views.deleteacc,name='deleteacc'),
    path('uparticle/<int:itmid>',views.uparticle,name='uparticle'),
]