# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0014_client_last_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='AAA_County',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='settings',
            name='AAA_Region',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='settings',
            name='AAA_VendorID',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='settings',
            name='AAA_VendorSite',
            field=models.CharField(max_length=4),
        ),
    ]
