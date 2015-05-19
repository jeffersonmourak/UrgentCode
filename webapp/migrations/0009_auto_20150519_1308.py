# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_answers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answers',
            options={'verbose_name': 'Resposta', 'verbose_name_plural': 'Respostas'},
        ),
        migrations.AddField(
            model_name='forums',
            name='question',
            field=models.TextField(default='', verbose_name=b'Pergunta'),
            preserve_default=False,
        ),
    ]
