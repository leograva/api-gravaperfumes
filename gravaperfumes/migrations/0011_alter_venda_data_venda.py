# Generated by Django 4.0.5 on 2022-07-25 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gravaperfumes', '0010_alter_estoque_perfume_alter_perfume_fabricante_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='data_venda',
            field=models.DateField(auto_now=True),
        ),
    ]