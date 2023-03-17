from django.db import models

# Create your models here.
class Libro_buy(models.Model):
    titulo = models.CharField(max_length=20)
    precio = models.IntegerField()

class Libro_sell(models.Model):
    titulo = models.CharField(max_length=20)
    precio = models.IntegerField()

class Libro_leído(models.Model):
    titulo = models.CharField(max_length=20)