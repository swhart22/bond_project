# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-22 16:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0006_auto_20160921_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='header',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]