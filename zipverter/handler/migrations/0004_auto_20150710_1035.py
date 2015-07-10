# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handler', '0003_locationtableauditlogentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggForLocationTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request', models.CharField(max_length=200)),
                ('response', models.CharField(max_length=200)),
                ('client_ip', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='locationtableauditlogentry',
            name='action_user',
        ),
        migrations.DeleteModel(
            name='LocationTableAuditLogEntry',
        ),
    ]
