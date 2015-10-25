# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='additional_races',
        ),
        migrations.AddField(
            model_name='client',
            name='multiracial',
            field=models.BooleanField(verbose_name='Multi-Racial', default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='multiracial_amind',
            field=models.BooleanField(verbose_name='American Indian Multi-Racial', default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='multiracial_asian',
            field=models.BooleanField(verbose_name='Asian Multi-Racial', default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='multiracial_black',
            field=models.BooleanField(verbose_name='Black Multi-Racial', default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='multiracial_white',
            field=models.BooleanField(verbose_name='White Multi-Racial', default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='audiologist',
            name='allowed',
            field=models.TextField(blank=True, null=True, help_text='How many clients are generally accepted and which provider(s)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='aids_requested_left',
            field=models.BooleanField(verbose_name='Hearing aid requested (left)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='aids_requested_right',
            field=models.BooleanField(verbose_name='Hearing aid requested (right)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='audient_id',
            field=models.CharField(verbose_name='Audient ID', blank=True, null=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='client',
            name='audiologist_invoiced_amount',
            field=models.DecimalField(validators=[django.core.validators.MinValueValidator(0)], max_digits=10, decimal_places=2, verbose_name='Audiologist invoiced amount ($)', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='cost_share',
            field=models.PositiveIntegerField(verbose_name='Cost share (%)', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='cost_share_approval',
            field=models.DateField(verbose_name='Cost share approval date', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='deliverable',
            field=models.BooleanField(verbose_name='Can accept mail', default=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='emergency_contact',
            field=models.CharField(verbose_name='Emergency contact name', blank=True, null=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='client',
            name='emergency_phone',
            field=localflavor.us.models.PhoneNumberField(verbose_name='Emergency contact phone', blank=True, null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='family_size',
            field=models.PositiveSmallIntegerField(default=1, help_text='Including client'),
        ),
        migrations.AlterField(
            model_name='client',
            name='is_hispanic',
            field=models.BooleanField(verbose_name='Is Hispanic'),
        ),
        migrations.AlterField(
            model_name='client',
            name='is_veteran',
            field=models.BooleanField(verbose_name='Veteran', default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=localflavor.us.models.PhoneNumberField(verbose_name='Phone number', blank=True, null=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='race',
            field=models.CharField(choices=[('White', 'White'), ('Black', 'Black'), ('Asian/Hawaiian/Pacific Islander', 'Asian/Hawaiian/Pacific Islander'), ('American Indian/Eskimo/Aleut', 'American Indian/Eskimo/Aleut')], max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='update_meeting',
            field=models.DateField(verbose_name='Update meeting date', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='incomesource',
            name='category',
            field=models.CharField(choices=[('Wages', 'Wages (Monthly)'), ('Social Security Statement', 'Social Security Statement (Monthly)'), ('Social Security Disability', 'Social Security Disability (Monthly)'), ('Social Security Income', 'Social Security Income (Monthly)'), ("Veteran's Benefits", "Veteran's Benefits (Monthly)"), ('Retirement Fund (401), IRA', 'Retirement Fund (401), IRA (Monthly)'), ('Annuities', 'Annuities'), ('Pension Statement', 'Pension Statement'), ('Checking Account Statement', 'Checking Account Statement'), ('Savings Account Statement', 'Savings Account Statement'), ('Mutual Fund Statement', 'Mutual Fund Statement'), ('Certificate Deposits', 'Certificate Deposits'), ('Stocks / Bonds', 'Stocks / Bonds')], max_length=255),
        ),
        migrations.AlterField(
            model_name='meetinglog',
            name='consultation_time',
            field=models.PositiveIntegerField(verbose_name='Consulation time (minutes)', default=15),
        ),
        migrations.AlterField(
            model_name='meetinglog',
            name='paperwork_time',
            field=models.PositiveIntegerField(verbose_name='Paperwork time (minutes)', default=15),
        ),
        migrations.AlterField(
            model_name='meetinglog',
            name='results',
            field=models.TextField(blank=True, help_text='Problems, solutions, progress, equipment, etc.'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='income_level_1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='settings',
            name='income_level_2',
            field=models.IntegerField(),
        ),
    ]
