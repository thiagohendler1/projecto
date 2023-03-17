from django.contrib import admin
from develop.models import Libro_leído, Libro_buy, Libro_sell

# Register your models here.
admin.site.register(Libro_leído)
admin.site.register(Libro_buy)
admin.site.register(Libro_sell)