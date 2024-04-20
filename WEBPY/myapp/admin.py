import imp
from django.contrib import admin

# Register your models here for see in administrator.
from .models import Category, Product, Rule,User

admin.site.register(Product,admin.ModelAdmin)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Rule)