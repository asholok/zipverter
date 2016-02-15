# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handler', '0004_locationtable_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationtable',
            name='timezone',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='loggforlocationtable',
            name='client_ip',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='loggforlocationtable',
            name='request',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='loggforlocationtable',
            name='response',
            field=models.CharField(max_length=256),
        ),
    ]
