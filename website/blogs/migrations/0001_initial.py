# Generated by Django 2.2 on 2019-06-21 11:10

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.IntegerField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(default='', max_length=200)),
                ('categories', models.CharField(default='', max_length=200)),
                ('abstract', models.CharField(default='', max_length=200)),
                ('views', models.IntegerField(default=0, editable=False)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('publishing_date', models.DateField(default=datetime.date.today)),
                ('author', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
