# Generated by Django 2.2 on 2019-06-19 09:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitments', '0002_auto_20190619_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantresponses',
            name='next_round_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 19, 14, 35, 26, 305986)),
        ),
    ]