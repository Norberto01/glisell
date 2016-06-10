# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 05:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('customers', '0001_initial'),
        ('lodging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Teléfono')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='EMail')),
                ('rnc', models.CharField(blank=True, max_length=255, verbose_name='RNC')),
                ('mobile', models.CharField(blank=True, max_length=255, null=True, verbose_name='Celular')),
                ('website', models.CharField(blank=True, max_length=255, null=True, verbose_name='Sitio Web')),
                ('notes', wagtail.wagtailcore.fields.RichTextField(blank=True, null=True, verbose_name='Notas')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FiscalPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre')),
                ('sequence', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='category.SequenceTypes', verbose_name='Secuencia')),
            ],
            options={
                'verbose_name': 'Posición Fiscal',
                'verbose_name_plural': 'Posiciónes Fiscales',
            },
        ),
        migrations.CreateModel(
            name='InternalContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Teléfono')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='EMail')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Cargo Laboral',
                'verbose_name_plural': 'Cargos Laborales',
            },
        ),
        migrations.CreateModel(
            name='CustomerBusinessRel',
            fields=[
                ('businesscontact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contacts.BusinessContact')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('business', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_business_rel', to='customers.Customer')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('contacts.businesscontact', models.Model),
        ),
        migrations.CreateModel(
            name='CustomerPersonalRel',
            fields=[
                ('internalcontact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contacts.InternalContact')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('personal', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_personal_rel', to='customers.Customer')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('contacts.internalcontact', models.Model),
        ),
        migrations.CreateModel(
            name='LodgingBusinessContact',
            fields=[
                ('businesscontact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contacts.BusinessContact')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('lodging', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='lodging_business', to='lodging.Lodging')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('contacts.businesscontact', models.Model),
        ),
        migrations.CreateModel(
            name='LodgingInternalContact',
            fields=[
                ('internalcontact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contacts.InternalContact')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('lodging', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='lodging_internal', to='lodging.Lodging')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('contacts.internalcontact', models.Model),
        ),
        migrations.AddField(
            model_name='internalcontact',
            name='job_position',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='contacts.JobPosition', verbose_name='Cargo Laboral'),
        ),
        migrations.AddField(
            model_name='businesscontact',
            name='fis_position',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='contacts.FiscalPosition', verbose_name='Posición Fiscal'),
        ),
    ]