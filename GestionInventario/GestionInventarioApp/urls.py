from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.main,name='mainpage'),
    path('categoria/',views.categoria,name='categoria'),
    path('price/',views.precio,name='precio')
    ]