# Generated by Django 2.2 on 2019-08-08 05:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20190808_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='event_time',
            field=models.TimeField(default=datetime.time(11, 10, 16, 164963)),
        ),
    ]
