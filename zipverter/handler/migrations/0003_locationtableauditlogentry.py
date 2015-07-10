# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('handler', '0002_auto_20150626_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationTableAuditLogEntry',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('country', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('action_id', models.AutoField(serialize=False, primary_key=True)),
                ('action_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('action_type', models.CharField(max_length=1, editable=False, choices=[('I', 'Created'), ('U', 'Changed'), ('D', 'Deleted')])),
                ('action_user', audit_log.models.fields.LastUserField(related_name='_locationtable_audit_log_entry', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-action_date',),
                'default_permissions': (),
            },
        ),
    ]
