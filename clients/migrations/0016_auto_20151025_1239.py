# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0015_client_county'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='county',
            field=models.CharField(default='Kent', max_length=64, choices=[('01', 'Alcona'), ('02', 'Alger'), ('03', 'Allegan'), ('04', 'Alpena'), ('05', 'Antrim'), ('06', 'Arenac'), ('07', 'Baraga'), ('08', 'Barry'), ('09', 'Bay'), ('10', 'Benzie'), ('11', 'Berrien'), ('12', 'Branch'), ('13', 'Calhoun'), ('14', 'Cass'), ('15', 'Charlevoix'), ('16', 'Cheboygan'), ('17', 'Chippewa'), ('18', 'Clare'), ('19', 'Clinton'), ('20', 'Crawford'), ('21', 'Delta'), ('22', 'Dickinson'), ('23', 'Eaton'), ('24', 'Emmet'), ('25', 'Genesee'), ('26', 'Gladwin'), ('27', 'Gogebic'), ('28', 'Grand Traverse'), ('29', 'Gratiot'), ('30', 'Hillsdale'), ('31', 'Houghton'), ('32', 'Huron'), ('33', 'Ingham'), ('34', 'Ionia'), ('35', 'Iosco'), ('36', 'Iron'), ('37', 'Isabella'), ('38', 'Jackson'), ('39', 'Kalamazoo'), ('40', 'Kalkaska'), ('41', 'Kent'), ('42', 'Keweenaw'), ('43', 'Lake'), ('44', 'Lapeer'), ('45', 'Leelanau'), ('46', 'Lenawee'), ('47', 'Livingston'), ('48', 'Luce'), ('49', 'Mackinac'), ('50', 'Macomb'), ('51', 'Manistee'), ('52', 'Marquette'), ('53', 'Mason'), ('54', 'Mecosta'), ('55', 'Menominee'), ('56', 'Midland'), ('57', 'Missaukee'), ('58', 'Monroe'), ('59', 'Montcalm'), ('60', 'Montmorency'), ('61', 'Muskegon'), ('62', 'Newaygo'), ('63', 'Oakland'), ('64', 'Oceana'), ('65', 'Ogemaw'), ('66', 'Ontonagon'), ('67', 'Osceola'), ('68', 'Oscoda'), ('69', 'Otsego'), ('70', 'Ottawa'), ('71', 'Presque Isle'), ('72', 'Roscommon'), ('73', 'Saginaw'), ('74', 'Sanilac'), ('75', 'Schoolcraft'), ('76', 'Shiawassee'), ('77', 'St. Clair'), ('78', 'St. Joseph'), ('79', 'Tuscola'), ('80', 'Van Buren'), ('81', 'Washtenaw'), ('82', 'Wayne'), ('83', 'Wexford'), ('84', 'Foreign')]),
        ),
    ]
