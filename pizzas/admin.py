from django.contrib import admin

# Register your models here.
from .models import Pizza, Ingrediente

admin.site.register(Pizza)
admin.site.register(Ingrediente)