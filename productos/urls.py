from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    # Catálogo principal
    path("", views.lista_productos, name="lista"),

    # Detalle de producto
    path("detalle/<int:producto_id>/", views.detalle_view, name="detalle"),

    # Carrito
    path("carrito/", views.ver_carrito_view, name="ver_carrito"),
    path("carrito/agregar/<int:producto_id>/", views.add_to_cart_view, name="add_to_cart"),
    path("carrito/vaciar/", views.vaciar_carrito_view, name="vaciar_carrito"),
]
