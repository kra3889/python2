# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-26 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beltlogin_set', '0002_auto_20180226_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pokenum',
            field=models.IntegerField(default=0),
        ),
    ]