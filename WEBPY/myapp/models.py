from django.db import models
from django.contrib.auth.models import User

class Rule(models.Model):
    SELECTION_RULE = (
        ('A', 'ADMIN'),
        ('E', 'EMPLEADO'),
        ('B', 'EMPLEADO_2'),
    )
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=10,choices=SELECTION_RULE)

    # Esto sirve en el administrador django se muestre la lista
    # de project por su nombre
    def __str__(self):
        return self.name

class User(models.Model):
    code = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    edad = models.IntegerField()
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE)
     
    def __str__(self):
        return self.first_name + '  -  ' + self.last_name




class Category(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name 
        
class Product(models.Model):
    SELECTION_TYPE = (
        ('L', 'LITROS'),
        ('M', 'METROS'),
        ('V', 'VOLUMEN'),
        ('U', 'UNIDAD'),
    )
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price_unit = models.FloatField() 
    quantity = models.FloatField()
    type_product = models.CharField(max_length=1, choices=SELECTION_TYPE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name + '  -  ' + self.category.name




class MOvUser_Product(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)