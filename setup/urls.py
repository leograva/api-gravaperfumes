from django.contrib import admin
from django.urls import path,include
from gravaperfumes.views import ClientesViewSet, FabricantesViewSet, PerfumesViewSet, VendasViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes',ClientesViewSet,basename ='Clientes')
router.register('fabricantes',FabricantesViewSet,basename ='Fabricantes')
router.register('perfumes',PerfumesViewSet,basename ='Perfumes')
router.register('vendas',VendasViewSet,basename='Vendas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('perfumes/<int:pk>/fabricante/', ListaPerfumesFabricante.as_view()),
    #path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
]
