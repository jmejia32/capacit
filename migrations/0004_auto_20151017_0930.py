# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacit', '0003_auto_20151017_0924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capacitacion',
            old_name='ccTrab',
            new_name='nombTrab',
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='cc',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='nombre',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
    ]
