# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-27 07:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0004_auto_20160627_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hits',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 7, 57, 15, 227874, tzinfo=utc)),
        ),
    ]
