# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0003_auto_20160618_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='like',
            field=models.IntegerField(default=False),
        ),
    ]