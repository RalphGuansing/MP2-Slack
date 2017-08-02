# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 08:47
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newbeginnings', '0014_auto_20170728_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='item_type_slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='item_type'),
        ),
        migrations.AddField(
            model_name='post',
            name='item_use_slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='item_use'),
        ),
        migrations.AlterField(
            model_name='post',
            name='item_condition_slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='item_condition'),
        ),
    ]