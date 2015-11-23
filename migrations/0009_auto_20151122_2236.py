# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacit', '0008_auto_20151017_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Parametro',
        ),
        migrations.DeleteModel(
            name='ValorParametro',
        ),
        migrations.RemoveField(
            model_name='capacitacion',
            name='ccTrab',
        ),
        migrations.AddField(
            model_name='asignacion',
            name='idCapacit',
            field=models.ForeignKey(related_name='Capacitacion', to='capacit.Capacitacion'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='idTrab',
            field=models.ForeignKey(related_name='Trabajador', to='capacit.Trabajador'),
        ),
    ]
