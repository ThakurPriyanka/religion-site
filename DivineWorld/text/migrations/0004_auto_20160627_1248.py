# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-27 07:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0003_auto_20160627_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hits',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 7, 18, 23, 139094, tzinfo=utc)),
        ),
    ]
