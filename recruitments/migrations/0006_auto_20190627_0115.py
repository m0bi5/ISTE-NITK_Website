# Generated by Django 2.2 on 2019-06-26 19:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitments', '0005_auto_20190627_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprogress',
            name='next_round_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 27, 1, 15, 35, 272158), null=True),
        ),
    ]