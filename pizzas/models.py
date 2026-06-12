from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Pizzas'

    def __str__(self):
        return self.name

class Ingrediente(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Ingredientes'
        ordering = ['name']

    def __str__(self):
        return self.name