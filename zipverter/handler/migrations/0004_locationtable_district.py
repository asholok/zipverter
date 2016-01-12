# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handler', '0003_locationtable_state_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationtable',
            name='district',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
