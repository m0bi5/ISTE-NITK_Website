# Generated by Django 2.2.8 on 2020-01-30 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0012_auto_20200130_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='end_time',
            field=models.TimeField(default=datetime.time(10, 2, 36, 607760)),
        ),
        migrations.AlterField(
            model_name='meet',
            name='start_time',
            field=models.TimeField(default=datetime.time(10, 2, 36, 607742)),
        ),
    ]
