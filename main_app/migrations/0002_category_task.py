# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('trust_level', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(editable=False)),
                ('category', models.CharField(max_length=50)),
                ('task', models.CharField(max_length=100)),
                ('notes', models.CharField(blank=True, max_length=200)),
                ('day_one', models.CharField(blank=True, default=None, max_length=3)),
                ('day_two', models.CharField(blank=True, default=None, max_length=3)),
                ('day_three', models.CharField(blank=True, default=None, max_length=3)),
                ('day_four', models.CharField(blank=True, default=None, max_length=3)),
                ('day_five', models.CharField(blank=True, default=None, max_length=3)),
                ('day_six', models.CharField(blank=True, default=None, max_length=3)),
                ('day_seven', models.CharField(blank=True, default=None, max_length=3)),
            ],
        ),
    ]
