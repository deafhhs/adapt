# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='additional_races',
            field=models.CharField(null=True, blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='client',
            name='audiologist',
            field=models.ForeignKey(null=True, blank=True, to='clients.Audiologist'),
        ),
        migrations.AlterField(
            model_name='client',
            name='audiologist_appointment_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='audiologist_referral_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='provider',
            field=models.ForeignKey(null=True, blank=True, to='clients.Provider'),
        ),
    ]
