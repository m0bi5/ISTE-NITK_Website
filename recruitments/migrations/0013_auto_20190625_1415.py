# Generated by Django 2.2 on 2019-06-25 08:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitments', '0012_auto_20190625_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprogress',
            name='next_round_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 25, 14, 15, 22, 842572), null=True),
        ),
    ]
