# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 14:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='integrent',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='step',
        ),
    ]
