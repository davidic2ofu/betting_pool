# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0046_auto_20171128_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedpick',
            name='week',
            field=models.IntegerField(default=0, verbose_name='Week in Season'),
        ),
    ]
