# Generated by Django 2.2.4 on 2020-01-28 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0068_auto_20200128_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloghits',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 17, 27, 7, 935254)),
        ),
    ]
