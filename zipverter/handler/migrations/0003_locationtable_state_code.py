# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handler', '0002_locationtable_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationtable',
            name='state_code',
            field=models.CharField(max_length=7, blank=True),
        ),
    ]
