# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=256)),
                ('major', models.CharField(max_length=256)),
                ('gender', models.CharField(max_length=256)),
                ('ethnicity', models.CharField(max_length=256)),
                ('residency', models.CharField(max_length=256)),
                ('high_school', models.CharField(max_length=256)),
            ],
        ),
    ]
