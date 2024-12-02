from django.contrib import admin
from .models import Productos , Eventos

    
class ProductosAdmin(admin.ModelAdmin):
    pass

class EventosAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Productos ,ProductosAdmin)
admin.site.register(Eventos ,EventosAdmin)

