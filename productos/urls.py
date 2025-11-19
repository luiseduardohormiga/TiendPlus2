from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path("", views.lista_productos, name="lista"),
    path("producto/<int:pk>/", views.detalle_producto, name="detalle"),
    path("producto/<int:pk>/add/", views.add_to_cart_and_recommend, name="agregar_carrito"),
    path("producto/<int:pk>/add/ajax/", views.add_to_cart_ajax, name="add_ajax"),
]