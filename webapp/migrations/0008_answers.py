# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20150519_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, verbose_name=b'Id', primary_key=True)),
                ('message', models.TextField(verbose_name=b'Mensagem')),
                ('forum', models.ForeignKey(verbose_name=b'Forum', to='webapp.Forums')),
                ('user', models.ForeignKey(verbose_name=b'Usu\xc3\xa1rio', to='webapp.Users')),
            ],
            options={
                'verbose_name': 'Inscrito',
                'verbose_name_plural': 'Inscritos',
            },
            bases=(models.Model,),
        ),
    ]
