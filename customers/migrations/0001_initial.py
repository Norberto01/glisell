# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 05:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientsTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo De Cliente',
                'verbose_name_plural': 'Tipos De Clientes',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customertype_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='category.CustomerType')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección')),
                ('client_type', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='customers.ClientsTypes', verbose_name='Tipo de cliente')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Agregar cliente',
            },
            bases=('category.customertype',),
        ),
    ]
