# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capacitacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identif', models.CharField(max_length=5)),
                ('nombre', models.CharField(max_length=20)),
                ('descrip', models.CharField(max_length=100)),
                ('objG', models.CharField(max_length=150)),
                ('objE', models.CharField(max_length=200)),
                ('fechaI', models.DateField()),
                ('fechaF', models.DateField()),
                ('tutor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cc', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ValorParametro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='capacitacion',
            name='ccTrab',
            field=models.ForeignKey(to='capacit.Trabajador'),
        ),
    ]
