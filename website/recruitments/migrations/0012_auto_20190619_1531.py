# Generated by Django 2.2 on 2019-06-19 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitments', '0011_auto_20190619_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantresponses',
            name='next_round_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 19, 15, 31, 28, 552020), null=True),
        ),
    ]
