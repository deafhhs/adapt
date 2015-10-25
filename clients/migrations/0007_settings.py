# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_auto_20151024_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('income_level_1', models.IntegerField(default=11770)),
                ('income_level_2', models.IntegerField(default=23540)),
            ],
            options={
                'verbose_name': 'Settings',
            },
        ),
    ]
