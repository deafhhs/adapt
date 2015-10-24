# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20151024_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='audiologist_invoicded_date',
            new_name='audiologist_invoiced_date',
        ),
    ]
