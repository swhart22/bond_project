# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-23 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0011_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
