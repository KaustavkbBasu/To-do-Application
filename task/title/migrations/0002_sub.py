# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-06 14:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('title', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ts', to='title.Task')),
            ],
        ),
    ]
