# Generated by Django 2.2 on 2019-06-21 07:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitments', '0020_auto_20190621_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprogress',
            name='next_round_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 21, 13, 1, 1, 625420), null=True),
        ),
    ]
