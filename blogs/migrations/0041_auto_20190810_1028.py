# Generated by Django 2.2 on 2019-08-10 04:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0040_auto_20190808_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloghits',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 10, 10, 28, 3, 993525)),
        ),
    ]