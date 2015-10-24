# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audiologist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('current', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('allowed', models.TextField(null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('audiologist_referral_date', models.DateField(null=True)),
                ('audiologist_appointment_date', models.DateField(null=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField(null=True, blank=True)),
                ('intake_date', models.DateField(auto_now_add=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('city', models.CharField(null=True, blank=True, max_length=64)),
                ('state', localflavor.us.models.USPostalCodeField(null=True, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FM', 'Federated States of Micronesia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MH', 'Marshall Islands'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PW', 'Palau'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], blank=True, max_length=2, default='MI')),
                ('zip_code', localflavor.us.models.USZipCodeField(null=True, blank=True, max_length=10)),
                ('deliverable', models.BooleanField(default=True)),
                ('email', models.EmailField(null=True, blank=True, max_length=254)),
                ('phone', localflavor.us.models.PhoneNumberField(null=True, blank=True, max_length=20)),
                ('spouse', models.CharField(null=True, blank=True, max_length=128)),
                ('is_veteran', models.BooleanField(default=False)),
                ('live_alone', models.BooleanField()),
                ('family_size', models.PositiveSmallIntegerField(default=1)),
                ('emergency_contact', models.CharField(null=True, blank=True, max_length=128)),
                ('emergency_phone', localflavor.us.models.PhoneNumberField(null=True, blank=True, max_length=20)),
                ('race', models.CharField(choices=[('AA', 'Afro. Amer.'), ('Al', 'Aleut'), ('As', 'Asian'), ('Es', 'Eskimo'), ('PI', 'Pac. Islander'), ('Wh', 'White'), ('O', 'Other')], max_length=2)),
                ('is_hispanic', models.BooleanField()),
                ('additional_races', models.CharField(max_length=256)),
                ('referrer', models.CharField(null=True, blank=True, max_length=256)),
                ('hearing_loss', models.PositiveSmallIntegerField(choices=[(1, 'Mild'), (2, 'Medium'), (3, 'Severe'), (4, 'Profound')])),
                ('aids_requested_left', models.BooleanField()),
                ('aids_requested_right', models.BooleanField()),
                ('equipment_requested', models.BooleanField()),
                ('equipment_borrowed', models.TextField(blank=True)),
                ('signed_client_intake', models.BooleanField()),
                ('signed_disclosure_authorization', models.BooleanField()),
                ('signed_confidentiality_policy', models.BooleanField()),
                ('signed_gross_annual_income', models.BooleanField()),
                ('signed_client_responsibility_fees', models.BooleanField()),
                ('audiologist', models.ForeignKey(to='clients.Audiologist')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='provider',
            field=models.ForeignKey(to='clients.Provider'),
        ),
    ]
