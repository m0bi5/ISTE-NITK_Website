# Generated by Django 2.2 on 2019-06-25 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitments', '0020_auto_20190625_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprogress',
            name='next_round_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 25, 14, 53, 51, 580769), null=True),
        ),
    ]
