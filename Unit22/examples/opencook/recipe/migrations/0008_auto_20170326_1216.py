# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 12:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_auto_20170324_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='created_date',
            new_name='created_at',
        ),
    ]
