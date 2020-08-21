from django.contrib import admin
from .models import Person, Documento, Venda


admin.site.register(Person)
admin.site.register(Documento)
admin.site.register(Venda)