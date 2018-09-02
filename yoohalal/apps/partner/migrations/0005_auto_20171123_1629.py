# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 09:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('partner', '0004_auto_20160107_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='users',
        ),
        migrations.AddField(
            model_name='partner',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Is Active?'),
        ),
        migrations.AddField(
            model_name='partner',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='partneraddress',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, verbose_name='Phone number'),
        ),
    ]
