from django.contrib import admin
from .models import Project , Task 

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("creado",) 

# Register your models here.
admin.site.register(Project)    
admin.site.register(Task ,TaskAdmin)

