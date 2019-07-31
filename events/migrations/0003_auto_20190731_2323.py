# Generated by Django 2.2 on 2019-07-31 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20190731_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(default='', max_length=200)),
                ('member1', models.CharField(default='', max_length=200)),
                ('member2', models.CharField(default='', max_length=200)),
                ('member3', models.CharField(default='', max_length=200)),
                ('first_place', models.BooleanField(default=False)),
                ('second_place', models.BooleanField(default=False)),
                ('third_place', models.BooleanField(default=False)),
                ('attendance', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='', max_length=12)),
            ],
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='event_time',
            field=models.TimeField(default=datetime.time(23, 23, 17, 746496)),
        ),
    ]
