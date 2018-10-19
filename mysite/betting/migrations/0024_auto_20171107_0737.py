# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 13:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0023_auto_20171106_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 13, 37, 46, 237733, tzinfo=utc), verbose_name='game time/date'),
        ),
        migrations.AlterField(
            model_name='game',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 13, 37, 46, 238234, tzinfo=utc), verbose_name='published'),
        ),
    ]
