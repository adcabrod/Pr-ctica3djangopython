# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20160923_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(null=True),
        ),
    ]