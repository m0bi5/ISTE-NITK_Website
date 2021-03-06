# Generated by Django 2.2.4 on 2020-01-23 18:46

import ckeditor_uploader.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', ckeditor_uploader.fields.RichTextUploadingField(default='Topic for the meet goes here')),
                ('date', models.DateField(default=datetime.date.today)),
                ('start_time', models.TimeField(default=datetime.time(18, 46, 47, 364228))),
                ('end_time', models.TimeField(default=datetime.time(18, 46, 47, 364286))),
                ('venue', models.CharField(default='ISTE Office', max_length=200)),
                ('sig', models.CharField(choices=[('Catalyst', 'Catalyst'), ('Chronicle', 'Chronicle'), ('Clutch', 'Clutch'), ('Create', 'Create'), ('Credit', 'Credit'), ('Concrete', 'Concrete'), ('Charge', 'Charge'), ('Crypt', 'Crypt'), ('Club', 'Club')], default='', max_length=12)),
                ('member', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
