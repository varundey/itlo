# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itlo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='state',
            field=models.CharField(choices=[(':thumbsup: The lab is *Open!*', 'Open'), ('Close', 'Close')], max_length=5),
        ),
    ]
