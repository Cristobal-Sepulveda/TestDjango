from django.urls import path 
from .views import home, ver, mostrar, form_crear_vehiculo, form_mod_vehiculo, form_del_vehiculo

urlpatterns=[ 
    path ('', home, name="home"),
    path ('ver/', ver, name="ver"),
    path ('mostrar/', mostrar, name="mostrar"),
    path ('form_crear_vehiculo/', form_crear_vehiculo, name="form_crear_vehiculo"),
    path ('form_mod_vehiculo/<id>', form_mod_vehiculo, name="form_mod_vehiculo"),
    path ('form_del_vehiculo/<id>', form_del_vehiculo, name="form_del_vehiculo"),
]