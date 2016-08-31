# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 14:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('purchased', models.DateTimeField(default=datetime.datetime(2016, 8, 30, 14, 52, 57, 740859, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('created', models.DateTimeField(default=datetime.datetime(2016, 8, 30, 14, 52, 57, 740167, tzinfo=utc))),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='habitat',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='workspace', to='zoo.Habitat'),
        ),
        migrations.AddField(
            model_name='animal',
            name='habitat',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='home', to='zoo.Habitat'),
        ),
    ]