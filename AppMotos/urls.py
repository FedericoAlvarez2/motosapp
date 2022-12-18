from django.urls import path
from AppMotos.views import *

urlpatterns = [
    path('', inicio, name="motos-inicio"),
    path('motos/', MotoCreateView.as_view(), name="motos"),
    path('motos/listado', MotoListView.as_view(), name="motos-listado"),
    path('motos/borrar/<pk>', MotoDeleteView.as_view(), name="motos-eliminar"),
    path('motos/editar/<pk>', MotoUpdateView.as_view(), name="motos-editar"),
    path('buscar/', ConsultaMotos, name="motos-buscar" )
]