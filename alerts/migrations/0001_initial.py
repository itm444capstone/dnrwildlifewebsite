# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('published', models.BooleanField(default=False)),
                ('recurring', models.BooleanField(default=False)),
                ('publish_date', models.DateTimeField()),
                ('publish_end_data', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Alerts',
                'verbose_name': 'Alert',
            },
            bases=(models.Model,),
        ),
    ]
