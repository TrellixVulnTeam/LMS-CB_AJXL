# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0001_initial'),
        ('courses', '0006_course_syllabus'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='assignments',
            field=models.ManyToManyField(blank=True, to='assignments.Assignment'),
        ),
    ]
