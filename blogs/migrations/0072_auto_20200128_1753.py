# Generated by Django 2.2.4 on 2020-01-28 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0071_auto_20200128_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloghits',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 17, 52, 59, 796043)),
        ),
    ]