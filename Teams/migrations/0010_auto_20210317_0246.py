# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-03-17 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0009_auto_20210317_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamregister',
            name='Captain_No',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='teamregister',
            name='Team_fee',
            field=models.CharField(blank=True, default=0, max_length=200),
        ),
    ]