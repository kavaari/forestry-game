# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-19 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forestry_game', '0002_auto_20171123_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='gas_consumption',
            field=models.FloatField(default=0),
        ),
    ]
