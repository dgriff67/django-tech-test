# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_company_po_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='region',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
