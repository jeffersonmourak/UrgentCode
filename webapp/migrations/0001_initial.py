# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, verbose_name=b'Id', primary_key=True)),
                ('message', models.TextField(verbose_name=b'Mensagem')),
            ],
            options={
                'verbose_name': 'Resposta',
                'verbose_name_plural': 'Respostas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, verbose_name=b'Id', primary_key=True)),
            ],
            options={
                'verbose_name': 'Seguidor',
                'verbose_name_plural': 'Seguidores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Forums',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, verbose_name=b'Id', primary_key=True)),
                ('name', models.CharField(max_length=45, verbose_name=b'Nome')),
                ('url', models.SlugField(verbose_name=b'URL')),
                ('descriptions', models.CharField(max_length=512, verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('question', models.TextField(verbose_name=b'Pergunta')),
            ],
            options={
                'verbose_name': 'Forum',
                'verbose_name_plural': 'Foruns',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, verbose_name=b'Id', primary_key=True)),
                ('answer', models.ForeignKey(verbose_name=b'Resposta', to='webapp.Answers')),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, verbose_name=b'Id', primary_key=True)),
                ('username', models.CharField(max_length=45, verbose_name=b'Nome de usu\xc3\xa1rio')),
                ('name', models.CharField(max_length=45, verbose_name=b'Nome')),
                ('surname', models.CharField(max_length=45, verbose_name=b'Sobrenome')),
                ('email', models.CharField(max_length=256, verbose_name=b'email')),
                ('password', models.CharField(max_length=256, verbose_name=b'Senha')),
                ('points', models.IntegerField(verbose_name=b'Pontos')),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(verbose_name=b'Usu\xc3\xa1rio', to='webapp.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='forums',
            name='creator',
            field=models.ForeignKey(verbose_name=b'Criador', to='webapp.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='followers',
            name='forum',
            field=models.ForeignKey(verbose_name=b'Forum', to='webapp.Forums'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='followers',
            name='user',
            field=models.ForeignKey(verbose_name=b'Usu\xc3\xa1rios', to='webapp.Users'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answers',
            name='forum',
            field=models.ForeignKey(verbose_name=b'Forum', to='webapp.Forums'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(verbose_name=b'Usu\xc3\xa1rio', to='webapp.Users'),
            preserve_default=True,
        ),
    ]
