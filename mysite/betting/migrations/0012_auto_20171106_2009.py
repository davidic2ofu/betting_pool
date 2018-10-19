# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 02:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0011_auto_20171106_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='betting_sheet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='betting.BettingSheet'),
        ),
        migrations.AlterField(
            model_name='game',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 2, 9, 21, 818564, tzinfo=utc), verbose_name='published'),
        ),
    ]
