# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 14:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0020_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinginformation',
            name='booking_id',
        ),
    ]
