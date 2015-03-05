# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0002_auto_20150305_1541'),
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=4, decimal_places=2)),
                ('ada', models.BooleanField(default=False)),
                ('alerts', models.ManyToManyField(to='alerts.Alert')),
                ('facilities', models.ManyToManyField(to='facilities.Facility')),
            ],
            options={
                'verbose_name': 'Site',
                'verbose_name_plural': 'Sites',
            },
            bases=(models.Model,),
        ),
    ]
