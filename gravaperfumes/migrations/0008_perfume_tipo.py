# Generated by Django 4.0.5 on 2022-07-09 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gravaperfumes', '0007_perfume_preco_custo_perfume_preco_venda'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfume',
            name='tipo',
            field=models.CharField(choices=[('EAI', 'Eau Intense'), ('EDC', 'Eau de Cologne'), ('EDT', 'Eau de Toilette'), ('EDP', 'Eau de Parfum'), ('P', 'Parfum')], default='EDT', max_length=3),
        ),
    ]