# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('icon', models.ImageField(upload_to='icons/')),
            ],
            options={
                'verbose_name_plural': 'Facilities',
                'verbose_name': 'Facility',
            },
            bases=(models.Model,),
        ),
    ]
