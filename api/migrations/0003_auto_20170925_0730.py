# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 07:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170925_0717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='last_lname',
            new_name='last_name',
        ),
    ]
