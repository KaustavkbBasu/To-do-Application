# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('title', '0004_sub_titles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sub',
            old_name='sub_task',
            new_name='task',
        ),
    ]