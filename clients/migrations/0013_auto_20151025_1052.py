# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0012_auto_20151025_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='non_kcsm',
            field=models.BooleanField(verbose_name='Non-KCSM'),
        ),
    ]
