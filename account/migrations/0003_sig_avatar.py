# Generated by Django 2.2 on 2019-07-02 06:38

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190701_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='sig',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=account.models.sig_avatar_path),
        ),
    ]
