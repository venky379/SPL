# Generated by Django 3.1.7 on 2021-03-27 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teams', '0011_auto_20210317_0342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team1', models.CharField(max_length=200)),
                ('Team2', models.CharField(max_length=200)),
                ('Winning_status', models.CharField(blank=True, default='', max_length=200)),
                ('Schedule_time', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
    ]
