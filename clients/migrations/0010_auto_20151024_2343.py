# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_auto_20151024_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='AAA_County',
            field=models.IntegerField(default=41),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='AAA_Region',
            field=models.IntegerField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='AAA_VendorID',
            field=models.IntegerField(default=38),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='AAA_VendorSite',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
