# Generated by Django 2.2 on 2019-06-19 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantresponses',
            name='next_round_time',
            field=models.DateField(default=datetime.datetime(2019, 6, 19, 14, 30, 50, 422017), null=True),
        ),
    ]