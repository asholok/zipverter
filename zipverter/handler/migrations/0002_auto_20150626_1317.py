# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handler', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='locationtable',
            unique_together=set([('country', 'zip_code')]),
        ),
    ]
