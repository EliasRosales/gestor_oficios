# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('nickname', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=80)),
                ('register_date', models.DateField(auto_now=True)),
                ('delete_date', models.DateField(blank=True, null=True)),
                ('password', models.CharField(max_length=255)),
                ('user_type', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
