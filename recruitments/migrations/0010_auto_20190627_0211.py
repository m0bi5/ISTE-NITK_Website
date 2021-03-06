# Generated by Django 2.2 on 2019-06-26 20:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitments', '0009_auto_20190627_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criteria',
            name='response',
        ),
        migrations.RemoveField(
            model_name='criteria',
            name='round',
        ),
        migrations.RemoveField(
            model_name='question',
            name='response',
        ),
        migrations.RemoveField(
            model_name='question',
            name='round',
        ),
        migrations.AddField(
            model_name='siground',
            name='criteria',
            field=models.ManyToManyField(to='recruitments.Criteria'),
        ),
        migrations.AddField(
            model_name='siground',
            name='questions',
            field=models.ManyToManyField(to='recruitments.Question'),
        ),
        migrations.AlterField(
            model_name='applicantprogress',
            name='next_round_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 6, 27, 2, 11, 33, 459365), null=True),
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitments.Applicant')),
            ],
        ),
    ]
