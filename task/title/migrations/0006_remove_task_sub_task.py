# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 16:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('title', '0005_auto_20180406_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='sub_task',
        ),
    ]
