# Generated by Django 2.2 on 2019-07-01 06:35

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sig',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]