# Generated by Django 2.2 on 2019-07-31 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0017_auto_20190731_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloghits',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 31, 23, 23, 17, 762388)),
        ),
    ]
