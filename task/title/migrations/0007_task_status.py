# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('title', '0006_remove_task_sub_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', max_length=200),
        ),
    ]
