# Generated by Django 2.2.8 on 2020-01-23 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0061_auto_20200117_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloghits',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 23, 18, 5, 5, 837820)),
        ),
    ]