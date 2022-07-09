from django.db import models

# Create your models here.
class Fabricante(models.Model):
    #CAMPOS
    nome = models.CharField(max_length=50)
    
    #CONSTRUTOR
    def __str__(self):
        return self.nome

class Perfume(models.Model):
    #CHOICES
    TAMANHOS = (('25ml','25ml'),('30ml','30ml'),('50ml','50ml'),('65ml','65ml'),('75ml','75ml'),('80ml','80ml'),('90ml','90ml'),('100ml','100ml'),('118ml','118ml'),('125ml','125ml'),('150ml','150ml'),('200ml','200ml')) 
    GENEROS = (('M','Masculino'),('F','Feminino'),('U','Unissex'))
    
    #CAMPOS
    nome = models.CharField(max_length=50)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
    tamanho = models.TextField(max_length=5,choices=TAMANHOS, blank=False,null=False,default='100ml')
    genero = models.CharField(max_length=1, choices=GENEROS, blank=False,null=False,default='M')
    
    #CONSTRUTOR
    def __str__(self):
        return self.nome

class Estoque(models.Model):
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=5, decimal_places=0)