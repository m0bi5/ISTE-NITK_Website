# Generated by Django 2.2 on 2019-06-24 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitments', '0006_auto_20190624_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprogress',
            name='next_round_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 24, 15, 16, 14, 924647), null=True),
        ),
    ]