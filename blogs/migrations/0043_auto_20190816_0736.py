# Generated by Django 2.2 on 2019-08-16 02:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0042_auto_20190810_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloghits',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 16, 7, 36, 57, 810856)),
        ),
    ]
