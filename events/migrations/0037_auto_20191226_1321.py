# Generated by Django 2.2.4 on 2019-12-26 13:21

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0036_auto_20191218_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Event Description goes here'),
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='event_time',
            field=models.TimeField(default=datetime.time(13, 21, 20, 185153)),
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='sig',
            field=models.CharField(choices=[('Catalyst', 'Catalyst'), ('Chronicle', 'Chronicle'), ('Clutch', 'Clutch'), ('Create', 'Create'), ('Credit', 'Credit'), ('Concrete', 'Concrete'), ('Charge', 'Charge'), ('Crypt', 'Crypt'), ('Club', 'Club')], default='', max_length=12),
        ),
    ]