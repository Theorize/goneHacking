# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_remove_status_trust_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='priority',
            field=models.IntegerField(default=5, max_length=20),
            preserve_default=False,
        ),
    ]
