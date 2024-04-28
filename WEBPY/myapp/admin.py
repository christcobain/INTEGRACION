#import imp
from django.contrib import admin

from .models import Sede, Rol, UnidadOrganica, Estado, Usuario, Funcionario, Movimiento, Proceso, Tipo_Bien, Bien, DetalleTransferencia, Asunto, DetalleSalida, DetalleProceso

# Register your models here for see in administrator.
# from .models import Category, Product, Rule,User

# admin.site.register(Product,admin.ModelAdmin)
# admin.site.register(Category)
# admin.site.register(User)
# admin.site.register(Rule)
#Nueva linea de codigo base
admin.site.register(Bien)
admin.site.register(Tipo_Bien)
admin.site.register(Estado)

admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Funcionario)
admin.site.register(Sede)
admin.site.register(UnidadOrganica)

admin.site.register(Proceso)
admin.site.register(Movimiento)
admin.site.register(DetalleProceso)

admin.site.register(DetalleTransferencia)

admin.site.register(DetalleSalida)
admin.site.register(Asunto)