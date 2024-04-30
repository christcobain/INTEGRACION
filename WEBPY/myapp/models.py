from django.db import models
from django.contrib.auth.models import User

class Sede(models.Model):
    nombre = models.CharField(max_length=50)

class Rol(models.Model):
    nombre = models.CharField(max_length=50)

class UnidadOrganica(models.Model):
    nombre = models.CharField(max_length=50)    

class Estado(models.Model):
    nombre = models.CharField(max_length=50)   
    
class Usuario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    dni = models.CharField(max_length=10)
    unidadOrganica = models.ForeignKey(UnidadOrganica, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    contrasena = models.CharField(max_length=20)

class Funcionario(models.Model):
    nombre = models.CharField(max_length=50)
    campo = models.CharField(max_length=20)
    unidadOrganica = models.ForeignKey(UnidadOrganica, on_delete=models.CASCADE)

class Movimiento(models.Model):
    nombre = models.CharField(max_length=50)

class Situacion(models.Model):
    nombre = models.CharField(max_length=50)

class Proceso(models.Model):
    movimiento = models.ForeignKey(Movimiento, on_delete=models.CASCADE)
    fechaIngreso = models.CharField(max_length=20)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    situacion = models.ForeignKey(Situacion, on_delete=models.CASCADE)
    fechaEliminacion = models.CharField(max_length=20)

class Descripcion(models.Model):
    nombre = models.CharField(max_length=50)


class Bien(models.Model):
    descripcion = models.ForeignKey(Descripcion, on_delete=models.CASCADE)
    ordenCompra = models.IntegerField()
    proveedor = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    serie = models.CharField(max_length=20)
    fechaVenGarantia = models.CharField(max_length=20)
    componentes = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    situacion = models.ForeignKey(Situacion, on_delete=models.CASCADE)

class DetalleTransferencia(models.Model):
    motivo = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)

class Asunto(models.Model):
    nombre = models.CharField(max_length=50)

class DetalleSalida(models.Model):
    asunto = models.ForeignKey(Asunto, on_delete=models.CASCADE)
    antecedentes = models.CharField(max_length=200)
    analisis = models.CharField(max_length=1000)
    conclusiones = models.CharField(max_length=300)
    recomendaciones = models.CharField(max_length=200)

class DetalleProceso(models.Model):
    proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)
    UsuarioInicial = models.CharField(max_length=20)
    unidadOrganicaInicial = models.CharField(max_length=20)
    sedeInicial = models.CharField(max_length=20)
    UsuarioFinal = models.CharField(max_length=20)
    unidadOrganicaFinal = models.CharField(max_length=20)
    sedeFinal = models.CharField(max_length=20)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE)
    detalleTransferencia = models.ForeignKey(DetalleTransferencia, on_delete=models.CASCADE)
    detalleSalida = models.ForeignKey(DetalleSalida, on_delete=models.CASCADE)

