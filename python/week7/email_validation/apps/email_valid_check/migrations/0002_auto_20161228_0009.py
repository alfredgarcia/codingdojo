# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 00:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('email_valid_check', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='email',
            managers=[
                ('emailMgr', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='email',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='email',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]