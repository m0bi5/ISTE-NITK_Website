# Generated by Django 2.2 on 2019-09-05 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0046_auto_20190905_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloghits',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 5, 11, 1, 18, 494782)),
        ),
    ]
