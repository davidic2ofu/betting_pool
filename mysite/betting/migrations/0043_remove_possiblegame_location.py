# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 04:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0042_auto_20171117_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='possiblegame',
            name='location',
        ),
    ]
