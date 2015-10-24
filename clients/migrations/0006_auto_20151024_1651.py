# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0005_auto_20151024_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='audiologist_invoiced_amount',
            field=models.DecimalField(decimal_places=2, blank=True, null=True, max_digits=10),
        ),
        migrations.AddField(
            model_name='client',
            name='data_entry_staff',
            field=models.ForeignKey(related_name='+', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='client',
            name='intake_staff',
            field=models.ForeignKey(related_name='+', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='client',
            name='proof_of_age',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='client',
            name='hearing_loss',
            field=models.CharField(choices=[('Mild', 'Mild'), ('Medium', 'Medium'), ('Severe', 'Severe'), ('Profound', 'Profound')], max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='race',
            field=models.CharField(choices=[('Afro. Amer.', 'Afro. Amer.'), ('Aleut', 'Aleut'), ('Asian', 'Asian'), ('Eskimo', 'Eskimo'), ('Pac. Islander', 'Pac. Islander'), ('White', 'White'), ('Other', 'Other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='incomesource',
            name='category',
            field=models.CharField(choices=[('Wages', 'Wages'), ('Social Security Statement', 'Social Security Statement'), ('Social Security Disability (SSD)', 'Social Security Disability (SSD)'), ('Social Security Income (SSI)', 'Social Security Income (SSI)'), ("Veteran's Benefits", "Veteran's Benefits"), ('Retirement Fund (401), IRA', 'Retirement Fund (401), IRA'), ('Annuities', 'Annuities'), ('Pension Statement', 'Pension Statement'), ('Checking Account Statement', 'Checking Account Statement'), ('Savings Account Statement', 'Savings Account Statement'), ('Mutual Fund Statement', 'Mutual Fund Statement'), ('Certificate Deposits (CD)', 'Certificate Deposits (CD)'), ('Stocks / Bonds', 'Stocks / Bonds')], max_length=255),
        ),
        migrations.AlterField(
            model_name='incomesource',
            name='source',
            field=models.CharField(choices=[('Client', 'Client'), ('Spouse', 'Spouse'), ('Other', 'Other')], max_length=255),
        ),
    ]
