from django.shortcuts import render
from . import models
# Create your views here.
def main(request):
    data = models.Producto.objects.all()
    return render(request,'Gestion/gestion.html',{'data':data})