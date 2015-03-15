# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='owner',
            field=models.CharField(max_length=70, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='owner_link',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='site',
            name='telephone',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
    ]
