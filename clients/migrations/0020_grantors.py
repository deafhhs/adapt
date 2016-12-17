# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0019_auto_20151025_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grantor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='grantors',
            field=models.ManyToManyField(to='clients.Grantor', blank=True),
        ),
    ]
