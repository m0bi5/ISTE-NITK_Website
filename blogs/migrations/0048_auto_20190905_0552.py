# Generated by Django 2.2.4 on 2019-09-05 05:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0047_auto_20190905_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloghits',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 5, 5, 52, 37, 193511)),
        ),
    ]