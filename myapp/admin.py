from django.contrib import admin
from .models import Productos, Eventos, EstadoCarta


class ProductosAdmin(admin.ModelAdmin):
    pass


class EventosAdmin(admin.ModelAdmin):
    pass


class EstadoCartaAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Eventos, EventosAdmin)
admin.site.register(EstadoCarta, EstadoCartaAdmin)
