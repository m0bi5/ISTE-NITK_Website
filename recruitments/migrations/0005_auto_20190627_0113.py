# Generated by Django 2.2 on 2019-06-26 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitments', '0004_auto_20190627_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprogress',
            name='next_round_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 27, 1, 13, 29, 910321), null=True),
        ),
    ]
