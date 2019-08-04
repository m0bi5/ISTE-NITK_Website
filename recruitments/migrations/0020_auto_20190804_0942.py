# Generated by Django 2.2 on 2019-08-04 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitments', '0019_auto_20190628_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantprogress',
            name='next_round_location',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='applicantprogress',
            name='interview_done',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='applicantprogress',
            name='qualified_for_next',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]