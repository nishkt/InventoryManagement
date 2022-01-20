from django.contrib import admin
from inventory.models import products, inventory
# Register your models here.

admin.site.register(products)
admin.site.register(inventory)