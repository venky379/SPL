# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-03-17 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0003_teamregister_team_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamregister',
            name='Team_slug',
            field=models.SlugField(default='', null=True),
        ),
    ]