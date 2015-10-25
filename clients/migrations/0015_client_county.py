# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0014_client_last_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='county',
            field=models.CharField(choices=[('Alcona', '01'), ('Alger', '02'), ('Allegan', '03'), ('Alpena', '04'), ('Antrim', '05'), ('Arenac', '06'), ('Baraga', '07'), ('Barry', '08'), ('Bay', '09'), ('Benzie', '10'), ('Berrien', '11'), ('Branch', '12'), ('Calhoun', '13'), ('Cass', '14'), ('Charlevoix', '15'), ('Cheboygan', '16'), ('Chippewa', '17'), ('Clare', '18'), ('Clinton', '19'), ('Crawford', '20'), ('Delta', '21'), ('Dickinson', '22'), ('Eaton', '23'), ('Emmet', '24'), ('Genesee', '25'), ('Gladwin', '26'), ('Gogebic', '27'), ('Grand Traverse', '28'), ('Gratiot', '29'), ('Hillsdale', '30'), ('Houghton', '31'), ('Huron', '32'), ('Ingham', '33'), ('Ionia', '34'), ('Iosco', '35'), ('Iron', '36'), ('Isabella', '37'), ('Jackson', '38'), ('Kalamazoo', '39'), ('Kalkaska', '40'), ('Kent', '41'), ('Keweenaw', '42'), ('Lake', '43'), ('Lapeer', '44'), ('Leelanau', '45'), ('Lenawee', '46'), ('Livingston', '47'), ('Luce', '48'), ('Mackinac', '49'), ('Macomb', '50'), ('Manistee', '51'), ('Marquette', '52'), ('Mason', '53'), ('Mecosta', '54'), ('Menominee', '55'), ('Midland', '56'), ('Missaukee', '57'), ('Monroe', '58'), ('Montcalm', '59'), ('Montmorency', '60'), ('Muskegon', '61'), ('Newaygo', '62'), ('Oakland', '63'), ('Oceana', '64'), ('Ogemaw', '65'), ('Ontonagon', '66'), ('Osceola', '67'), ('Oscoda', '68'), ('Otsego', '69'), ('Ottawa', '70'), ('Presque Isle', '71'), ('Roscommon', '72'), ('Saginaw', '73'), ('Sanilac', '74'), ('Schoolcraft', '75'), ('Shiawassee', '76'), ('St. Clair', '77'), ('St. Joseph', '78'), ('Tuscola', '79'), ('Van Buren', '80'), ('Washtenaw', '81'), ('Wayne', '82'), ('Wexford', '83'), ('Foreign', '84')], default='Kent', max_length=64),
        ),
    ]
