# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 05:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0043_remove_possiblegame_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='possiblegame',
            name='date',
            field=models.CharField(default=datetime.datetime(2017, 11, 17, 23, 28, 39, 658482), max_length=200),
            preserve_default=False,
        ),
    ]
