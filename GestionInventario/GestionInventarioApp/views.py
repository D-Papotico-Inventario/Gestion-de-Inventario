from django.shortcuts import render,redirect
from . import models

from .forms import Addform

# Create your views here.
def main(request):
    data = models.Producto.objects.all()
    return render(request,'Gestion/gestion.html',{'data':data})

def categoria(request):
    data = models.Producto.objects.all().order_by('categoria')
    return render (request,'Gestion/gestion.html',{'data':data})

def precio(request):
    data = models.Producto.objects.filter().order_by('price')
    return render (request,'Gestion/gestion.html',{'data':data})

def tiempo(request):
    data = models.Producto.objects.filter().order_by('created')

    return render (request,'Gestion/gestion.html',{'data':data})


def search(request):
    data = request.GET['search']
    data = models.Producto.objects.filter(name__icontains = data)
    return render(request,"Gestion/gestion.html",{"data":data})

def anadir(request):
    form = Addform()
    if request.method == 'POST':
        form = Addform(request.POST)
        if form.is_valid():
            producto = form.save()
            try:
                return redirect('/?producto_guardado')
            except:
                return redirect('/?algo_salio_mal')
        else:
            form = Addform()

    return render(request,'Gestion/addPdt.html',{'form':form})

def editar(request,id):
    producto = models.Producto.objects.get(id = id)
    form = Addform(request.POST,instance=producto)
    if form.is_valid():
        form.save()
        try:
            return redirect('/?producto_actualizado')
        except:
            return redirect('/?algo_salio_mal')
    else:
        form = Addform(instance=producto)
    return render(request,'Gestion/editar.html',{'form':form})

def eliminar(request,id):
    producto = models.Producto.objects.get(id = id)
    producto.delete()
    return redirect ('/?producto_eliminado')