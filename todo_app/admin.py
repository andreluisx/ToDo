from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Lista

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'detalhes')  # Campos que você quer exibir na lista de objetos

admin.site.register(Lista, MyModelAdmin)