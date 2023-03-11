from django.db import models

# Create your models here.

class Categoria (models.Model): 
    name = models.CharField(max_length=30)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Producto (models.Model): 
    name = models.CharField(max_length=30)
    codigos_costo = (
        ('1', 'Muy Barato'),
        ('2', 'Barato'),
        ('3', 'Intermedio'),
        ('4', 'Alto'),
        ('5', 'Muy Alto'),
    )
    categoria = models.ManyToManyField(Categoria)
    price = models.FloatField()
    cantidad = models.IntegerField()
    codigo_costo = models.CharField(choices= codigos_costo, max_length=25)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)



