from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def ver(request):
    return render (request, 'valida.html')

def mostrar(request):

    vehiculos = Vehiculo.objects.all()
    datos = {
        'vehiculos' : vehiculos
    }
    return render(request, 'mostrar.html', datos)

def form_crear_vehiculo(request):
    if request.method=='POST':
        vehiculo_form = VehiculoForm(request.POST)
        if vehiculo_form.is_valid():
            vehiculo_form.save()        #similar al insert
            return redirect('mostrar')
    else:
        vehiculo_form=VehiculoForm()
    return render(request, 'form_crear_vehiculo.html', {'vehiculo_form': vehiculo_form})
    
def form_mod_vehiculo(request, id):
    vehiculo =Vehiculo.objects.get(patente=id)
    datos = {
        'form': VehiculoForm(instance = vehiculo)
    }
    if request.method=='POST':
        formulario = VehiculoForm(data=request.POST, instance = vehiculo)
        if formulario.is_valid():
            formulario.save()
            return redirect('mostrar')
    return render(request, 'form_mod_vehiculo.html', datos)

def form_del_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect('mostrar')


