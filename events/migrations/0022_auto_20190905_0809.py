# Generated by Django 2.2 on 2019-09-05 02:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0021_auto_20190816_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='event_time',
            field=models.TimeField(default=datetime.time(8, 9, 15, 979048)),
        ),
    ]