from django.urls import path
from . import views  
urlpatterns = [
    path('new', views.new),
    path('home',views.home, name='home'),
    path('contact',views.contact,name='contact'),
    path('images', views.images, name='images'),
    path('about', views.about, name='about')
]


