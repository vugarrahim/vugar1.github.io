# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_auto_20160225_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingcargoitem',
            name='is_arrived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookingpassengeritem',
            name='is_arrived',
            field=models.BooleanField(default=False),
        ),
    ]