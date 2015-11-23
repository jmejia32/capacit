# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('capacit', '0007_auto_20151017_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capacitacion',
            name='objE',
        ),
        migrations.RemoveField(
            model_name='capacitacion',
            name='objG',
        ),
    ]
