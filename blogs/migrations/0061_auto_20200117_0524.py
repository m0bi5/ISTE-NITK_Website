# Generated by Django 2.2.8 on 2020-01-17 05:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0060_auto_20200115_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloghits',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 17, 5, 24, 24, 981359)),
        ),
    ]
