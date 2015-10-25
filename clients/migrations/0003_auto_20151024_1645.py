# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20151024_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source', models.CharField(max_length=1, choices=[('C', 'Client'), ('S', 'Spouse'), ('O', 'Other')])),
                ('category', models.CharField(max_length=3, choices=[('W', 'Wages'), ('SSS', 'Social Security Statement'), ('SSD', 'Social Security Disability (SSD)'), ('SSI', 'Social Security Income (SSI)'), ('VB', "Veteran's Benefits"), ('401', 'Retirement Fund (401), IRA'), ('A', 'Annuities'), ('PS', 'Pension Statement'), ('CAS', 'Checking Account Statement'), ('SAS', 'Savings Account Statement'), ('MFS', 'Mutual Fund Statement'), ('CD', 'Certificate  Deposits (CD)'), ('SB', 'Stocks / Bonds')])),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.RenameField(
            model_name='client',
            old_name='live_alone',
            new_name='lives_alone',
        ),
        migrations.AddField(
            model_name='client',
            name='audient_id',
            field=models.CharField(max_length=16, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='audiologist_invoicded_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='cost_share',
            field=models.DecimalField(max_digits=10, null=True, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='cost_share_approval',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='provider_auth_recv',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='provider_auth_sent',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='update_meeting',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='incomesource',
            name='client',
            field=models.ForeignKey(to='clients.Client'),
        ),
        migrations.AlterUniqueTogether(
            name='incomesource',
            unique_together=set([('client', 'source', 'category')]),
        ),
    ]
