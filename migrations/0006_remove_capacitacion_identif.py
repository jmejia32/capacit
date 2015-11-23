# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacit', '0005_auto_20151017_0933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capacitacion',
            name='identif',
        ),
    ]
