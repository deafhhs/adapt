# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_client_napis_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='non_kcsm',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='napis_id',
            field=models.CharField(max_length=11, verbose_name='NAPIS ID', null=True, blank=True),
        ),
    ]
