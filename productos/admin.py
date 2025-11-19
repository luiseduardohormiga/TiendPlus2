from django.contrib import admin
from .models import Categoria, Producto
from django.utils.html import format_html

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio", "stock", "categoria", "preview")
    list_filter = ("categoria",)
    search_fields = ("nombre",)
    ordering = ("nombre",)
    list_editable = ("precio", "stock", "categoria")
    readonly_fields = ("preview",)
    fields = ("nombre", "precio", "stock", "categoria", "imagen", "preview")

    def preview(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" width="80" style="border-radius:5px;" />',
                obj.imagen.url
            )
        return "(Sin imagen)"