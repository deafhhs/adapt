# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0018_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='napis_id',
            field=models.CharField(verbose_name='KCSM ID', null=True, blank=True, max_length=11),
        ),
    ]
