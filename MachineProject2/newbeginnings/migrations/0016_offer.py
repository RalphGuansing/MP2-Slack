# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 05:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newbeginnings', '0015_auto_20170728_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isPurchase', models.BooleanField(default=True)),
                ('purchase_offer', models.IntegerField(default=0)),
                ('isAccept', models.BooleanField(default=False)),
                ('exchange_offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exchange_post', to='newbeginnings.Post')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original_post', to='newbeginnings.Post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
