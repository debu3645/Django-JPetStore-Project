# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-14 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinyfinalapp', '0005_auto_20170213_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='vinyitems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vpid', models.CharField(max_length=10, null=True)),
                ('vitemid', models.CharField(max_length=20, null=True)),
                ('vdesc', models.CharField(max_length=50, null=True)),
                ('vprice', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]