# Generated by Django 2.2.8 on 2020-01-30 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('easy', models.CharField(default='[]', max_length=100)),
                ('med', models.CharField(default='[]', max_length=100)),
                ('hard', models.CharField(default='[]', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('pwd', models.CharField(default='iste', max_length=100)),
                ('points', models.IntegerField(default=25)),
                ('lives', models.IntegerField(default=3)),
                ('easy', models.BooleanField(default=True)),
                ('med', models.BooleanField(default=False)),
                ('hard', models.BooleanField(default=False)),
                ('subs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obscura.Submission')),
            ],
        ),
    ]
