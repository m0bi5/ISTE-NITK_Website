# Generated by Django 2.2.4 on 2020-01-28 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0002_auto_20200128_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='end_time',
            field=models.TimeField(default=datetime.time(17, 27, 7, 937731)),
        ),
        migrations.AlterField(
            model_name='meet',
            name='start_time',
            field=models.TimeField(default=datetime.time(17, 27, 7, 937701)),
        ),
    ]