# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20170125_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='care_of_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]