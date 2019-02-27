from django.contrib import admin
from .models import Banda, Integrantes, Album

# Register your models here.

admin.site.register(Album)
admin.site.register(Banda)
admin.site.register(Integrantes)