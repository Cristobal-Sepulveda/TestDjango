from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria= models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Nombre de Categoría')

    def __str__(self):
        return self.nombreCategoria


class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True, verbose_name='Patente')
    marca= models.CharField(max_length=20, verbose_name='Marca')
    modelo=models.CharField(max_length=20, verbose_name='Modelo')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')

    def __str__(self):
        return self.patente
