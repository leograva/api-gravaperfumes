from django.db import models

# Create your models here.
class Fabricante(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Perfume(models.Model):
    TAMANHOS = (('25ml','25ml'),('30ml','30ml'),('50ml','50ml'),('65ml','65ml'),('75ml','75ml'),('80ml','80ml'),('90ml','90ml'),('100ml','100ml'),('118ml','118ml'),('125ml','125ml'),('150ml','150ml'),('200ml','200ml')) 
    GENEROS = (('M','Masculino'),('F','Feminino'),('U','Unissex'))
    TIPOS = (('EAI','Eau Intense'),('EDC','Eau de Cologne'),('EDT','Eau de Toilette'),('EDP','Eau de Parfum'),('P','Parfum'))
    
    nome = models.CharField(max_length=50)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.PROTECT)
    tamanho = models.TextField(max_length=5,choices=TAMANHOS, blank=False,null=False,default='100ml')
    genero = models.CharField(max_length=1, choices=GENEROS, blank=False,null=False,default='M')
    tipo = models.CharField(max_length=3, choices=TIPOS, blank=False,null=False,default='EDT')
    
    def __str__(self):
        return '__all__'

class Estoque(models.Model):
    perfume = models.ForeignKey(Perfume, on_delete=models.PROTECT)
    quantidade = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        return '__all__'

class Venda(models.Model):
    perfume = models.ForeignKey(Perfume, on_delete=models.PROTECT) 
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT) 
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateField(auto_now=True)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, ' ')))
        return ' - '.join(field_values)