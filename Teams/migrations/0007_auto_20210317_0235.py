# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-03-17 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0006_auto_20210317_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamregister',
            name='Team_slug',
            field=models.SlugField(default='', null=True),
        ),
    ]
