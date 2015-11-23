# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacit', '0004_auto_20151017_0930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capacitacion',
            old_name='nombTrab',
            new_name='ccTrab',
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='cc',
            field=models.CharField(max_length=20, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]
