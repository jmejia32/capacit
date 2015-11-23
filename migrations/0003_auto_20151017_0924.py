# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacit', '0002_auto_20151017_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='ccTrab',
            field=models.ForeignKey(related_name='Trabajador', to='capacit.Trabajador'),
        ),
    ]
