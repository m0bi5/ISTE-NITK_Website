# Generated by Django 2.2.3 on 2019-07-31 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0016_merge_20190730_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloghits',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 31, 13, 54, 10, 455596)),
        ),
    ]
