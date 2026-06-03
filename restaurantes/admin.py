from django.contrib import admin
from .models import TipoComida, Restaurante

@admin.register(TipoComida)
class TipoComidaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'activo']
    search_fields = ['nombre']

@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'direccion', 'telefono', 'tipo_comida']
    search_fields = ['nombre']