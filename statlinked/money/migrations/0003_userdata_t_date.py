# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-25 07:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0002_auto_20180223_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='t_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
