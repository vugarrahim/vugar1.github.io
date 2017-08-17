# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0032_auto_20160304_1150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'permissions': (('bookingcheckin_view', 'Can check in Booking'),)},
        ),
        migrations.AlterField(
            model_name='bookingpassengeritem',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2, verbose_name='Gender'),
        ),
    ]