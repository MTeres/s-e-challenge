# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 16:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('term', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('date', models.DateTimeField()),
            ],
        ),
    ]