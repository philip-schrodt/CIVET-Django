# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djciv_data', '0011_auto_20150831_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='caselocs',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
