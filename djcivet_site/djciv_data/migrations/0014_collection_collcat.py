# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-12 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djciv_data', '0013_remove_case_caselocs'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='collcat',
            field=models.CharField(default={}, max_length=2000),
            preserve_default=False,
        ),
    ]
