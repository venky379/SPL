# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2021-03-14 08:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=200)),
                ('AadhaarNo', models.CharField(max_length=200)),
                ('Age', models.IntegerField(default=0)),
                ('play_to', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Teams.TeamRegister')),
            ],
        ),
    ]