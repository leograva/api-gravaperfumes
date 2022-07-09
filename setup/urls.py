from django.contrib import admin
from django.urls import path,include
#from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from gravaperfumes.views import EstoquesViewSet, FabricantesViewSet, PerfumesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('fabricantes',FabricantesViewSet,basename ='Fabricantes')
router.register('perfumes',PerfumesViewSet,basename ='Perfumes')
router.register('estoques',EstoquesViewSet,basename ='Estoques')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    #path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
]
