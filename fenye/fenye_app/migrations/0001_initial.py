# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-22 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=20)),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
    ]
