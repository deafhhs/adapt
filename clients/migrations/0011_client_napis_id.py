# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_auto_20151024_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='napis_id',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
