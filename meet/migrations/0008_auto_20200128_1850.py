# Generated by Django 2.2.4 on 2020-01-28 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0007_auto_20200128_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='end_time',
            field=models.TimeField(default=datetime.time(18, 50, 19, 839621)),
        ),
        migrations.AlterField(
            model_name='meet',
            name='start_time',
            field=models.TimeField(default=datetime.time(18, 50, 19, 839586)),
        ),
    ]
