# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_course_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_description',
            field=models.TextField(blank=True),
        ),
    ]
