# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0004_auto_20151024_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('contact_date', models.DateField()),
                ('consultation_time', models.PositiveIntegerField(default=15)),
                ('paperwork_time', models.PositiveIntegerField(default=15)),
                ('results', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='intake_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='meetinglog',
            name='client',
            field=models.ForeignKey(to='clients.Client'),
        ),
        migrations.AddField(
            model_name='meetinglog',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
