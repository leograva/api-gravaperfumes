from django.contrib import admin
from gravaperfumes.models import Estoque, Perfume, Fabricante

# Register your models here.
class Fabricantes(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id','nome')
    search_fields = ['nome']
    list_per_page = 20

admin.site.register(Fabricante, Fabricantes)

class Perfumes(admin.ModelAdmin):
    list_display = ('id','nome','fabricante','tamanho')
    list_display_links = ('id','nome','fabricante','tamanho')
    search_fields = ['id','nome','fabricante']
    list_per_page = 20

admin.site.register(Perfume, Perfumes)

class Estoques(admin.ModelAdmin):
    list_display = ('perfume','quantidade')
    list_display_links = ('perfume','quantidade')
    search_fields = ('perfume','quantidade')
    list_per_page = 20

admin.site.register(Estoque, Estoques)