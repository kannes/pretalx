# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0004_auto_20170902_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='recording_source',
            field=models.CharField(blank=True, choices=[('VOC', 'media.ccc.de')], max_length=3, null=True, verbose_name='Recording Source'),
        ),
        migrations.AddField(
            model_name='submission',
            name='recording_url',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Recording URL'),
        ),
    ]