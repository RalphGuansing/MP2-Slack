# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 09:00
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('newbeginnings', '0019_auto_20170812_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='exchange_offer',
            field=smart_selects.db_fields.GroupedForeignKey(group_field='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='newbeginnings.Post'),
        ),
    ]
