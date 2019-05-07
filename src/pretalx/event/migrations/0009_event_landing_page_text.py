# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 15:32
from __future__ import unicode_literals

from django.db import migrations
import i18nfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0008_event_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='landing_page_text',
            field=i18nfield.fields.I18nTextField(blank=True, null=True),
        ),
    ]
