# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-19 17:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bond', '0002_article_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='url',
        ),
    ]