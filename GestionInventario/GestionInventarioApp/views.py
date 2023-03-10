from django.shortcuts import render
from . import models
# Create your views here.
def main(request):
    data = models.Producto.objects.all()
    return render(request,'Gestion/gestion.html',{'data':data})

def categoria(request):
    data = models.Categoria.objects.filter().order_by('name')
    return render (request,'Gestion/gestion.html',{'data':data})

def precio(request):
    data = models.Producto.objects.filter().order_by('price')
    return render (request,'Gestion/gestion.html',{'data':data})

def search(request):
    data = request.GET['search']
    data = models.Producto.objects.filter(name__icontains = data)
    return render(request,"Gestion/gestion.html",{"data":data})