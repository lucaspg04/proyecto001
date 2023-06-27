from django.urls import path

from .views import agregar_producto, eliminar_producto, limpiar, restar_producto

app_name="carro"

urlpatterns = [
    path("agregar/<int:id>/", agregar_producto, name="agregar"),
    path("eliminar/<int:id>/", eliminar_producto, name="eliminar"),
    path("restar/<int:id>/", restar_producto, name="restar"),
    path("limpiar/", limpiar, name="limpiar"),
]
