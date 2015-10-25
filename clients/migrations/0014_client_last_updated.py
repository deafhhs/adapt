# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0013_auto_20151025_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='last_updated',
            field=models.DateField(auto_now=True, default=datetime.date(2015, 10, 25)),
            preserve_default=False,
        ),
    ]
