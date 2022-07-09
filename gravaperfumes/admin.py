from django.contrib import admin
from gravaperfumes.models import Estoque, Perfume, Fabricante, Cliente

# Register your models here.
class Fabricantes(admin.ModelAdmin):
    list_display = ['nome',]
    list_display_links = ['nome',]
    search_fields = ['nome',]
    list_per_page = 20

admin.site.register(Fabricante, Fabricantes)

class Perfumes(admin.ModelAdmin):
    list_display = ('nome','fabricante','tamanho','tipo','preco_custo','preco_venda')
    list_display_links = ('nome','fabricante','tamanho','tipo','preco_custo','preco_venda')
    search_fields = ['nome','fabricante']
    list_per_page = 20

admin.site.register(Perfume, Perfumes)

class Clientes(admin.ModelAdmin):
    list_display = ('nome',)
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Cliente, Clientes)