
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('home', views.home),
    path('first',views.first, name='first'),
    path('facebook',views.facebook, name='facebook'),
    path('calculater',views.calculater, name='calculater')
]
