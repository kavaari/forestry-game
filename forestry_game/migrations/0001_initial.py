# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-24 09:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(auto_now=True)),
                ('mapdata', models.TextField(default='')),
                ('mapinfo', models.TextField(default='')),
                ('svg', models.TextField(default='')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('distance', models.FloatField(default=0)),
                ('gas_consumption', models.FloatField(default=0)),
                ('duration', models.IntegerField(default=0)),
                ('logs', models.TextField(default='')),
                ('driving_unloaded_time', models.IntegerField(default=0)),
                ('driving_loaded_time', models.IntegerField(default=0)),
                ('loading_and_unloading', models.IntegerField(default=0)),
                ('idling', models.IntegerField(default=0)),
                ('driving_forward', models.FloatField(default=0)),
                ('reverse', models.FloatField(default=0)),
                ('driving_unloaded_distance', models.FloatField(default=0)),
                ('driving_loaded_distance', models.FloatField(default=0)),
                ('fuel_cost', models.FloatField(default=0)),
                ('worker_salary', models.FloatField(default=0)),
                ('loads_transported', models.IntegerField(default=0)),
                ('logs_deposited', models.IntegerField(default=0)),
                ('total_volume', models.FloatField(default=0)),
                ('productivity', models.FloatField(default=0)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forestry_game.Level')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
