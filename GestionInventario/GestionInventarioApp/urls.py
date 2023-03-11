from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.main,name='mainpage'),
    path('categoria/',views.categoria,name='categoria'),
    path('price/',views.precio,name='precio'),
    path('resultado/',views.search),
    path('añadir/',views.anadir,name='add'),
    path('editar/<int:id>',views.editar,name='editar'),
    path('eliminar/<int:id>',views.eliminar,name='eliminar'),
    path('tiempo/',views.tiempo,name='tiempo')


    ]