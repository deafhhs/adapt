# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import localflavor.us.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_auto_20151024_1651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='provider_auth_recv',
            new_name='provider_auth_received',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='provider_auth_sent',
            new_name='provider_auth_requested',
        ),
        migrations.AddField(
            model_name='client',
            name='adaptive_equipment',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='hearing_aid_assistance',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='hearing_assistance',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='quota_client',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='audiologist_invoiced_amount',
            field=models.DecimalField(max_digits=10, blank=True, validators=[django.core.validators.MinValueValidator(0)], null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='cost_share',
            field=models.PositiveIntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='data_entry_staff',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='client',
            name='hearing_loss',
            field=models.CharField(max_length=255, choices=[('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe'), ('Profound', 'Profound')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='intake_staff',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='client',
            name='renewal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='client',
            name='state',
            field=localflavor.us.models.USPostalCodeField(default='MI', max_length=2, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FM', 'Federated States of Micronesia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MH', 'Marshall Islands'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PW', 'Palau'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='zip_code',
            field=localflavor.us.models.USZipCodeField(max_length=10),
        ),
    ]
