# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacit', '0006_remove_capacitacion_identif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacitacion',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
