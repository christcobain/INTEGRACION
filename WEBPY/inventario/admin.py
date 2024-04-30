from django.contrib import admin

# Register your models here for see in administrator.
from .models import Usuario,UnidadOrganica,Sede,Estado,Rol
admin.site.register(Usuario)
admin.site.register(UnidadOrganica)
admin.site.register(Sede)
admin.site.register(Estado)
admin.site.register(Rol)