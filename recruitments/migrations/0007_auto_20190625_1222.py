# Generated by Django 2.2 on 2019-06-25 06:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitments', '0006_auto_20190625_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprogress',
            name='next_round_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 25, 12, 22, 10, 193089), null=True),
        ),
    ]
