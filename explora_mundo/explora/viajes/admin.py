
# Register your models here.
from django.contrib import admin
from django.contrib import admin
from .models import Destino, Paquete, Reserva

@admin.register(Destino)
class DestinoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio_base', 'duracion_recomendada', 'created_at')
    search_fields = ('nombre',)
    list_filter = ('duracion_recomendada',)

@admin.register(Paquete)
class PaqueteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'destino', 'precio', 'activo')
    list_filter = ('activo', 'destino')
    search_fields = ('nombre',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente_nombre', 'paquete', 'fecha_inicio', 'estado')
    list_filter = ('estado',)
    search_fields = ('cliente_nombre', 'cliente_email')
