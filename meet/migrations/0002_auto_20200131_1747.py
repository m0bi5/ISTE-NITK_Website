# Generated by Django 2.2.4 on 2020-01-31 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meet',
            name='end_time',
            field=models.TimeField(default=datetime.time(17, 47, 3, 59431)),
        ),
        migrations.AlterField(
            model_name='meet',
            name='start_time',
            field=models.TimeField(default=datetime.time(17, 47, 3, 59374)),
        ),
    ]
