# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 19:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20171201_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='assignments',
        ),
    ]