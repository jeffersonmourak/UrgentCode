#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.template.defaultfilters import slugify

class Users(models.Model):
	id = models.AutoField(verbose_name="Id",unique=True,primary_key=True)

	username = models.CharField(verbose_name="Nome de usuário", max_length=45)
	name = models.CharField(verbose_name="Nome", max_length=45)
	surname = models.CharField(verbose_name="Sobrenome", max_length=45)
	email = models.CharField(verbose_name="email", max_length=256)
	password = models.CharField(verbose_name="Senha", max_length=256)
	points = models.IntegerField(verbose_name="Pontos")

	class Meta:
		verbose_name = "Usuário"
		verbose_name_plural = "Usuários"

	def __str__(self):
		return self.name.encode("utf8")


class Forums(models.Model):
	id = models.AutoField(verbose_name="Id",unique=True,primary_key=True)
	
	name = models.CharField(verbose_name="Nome", max_length=45)
	creator = models.ForeignKey(Users,verbose_name="Criador")
	url = models.SlugField(verbose_name="URL")
	descriptions = models.CharField(verbose_name="Descrição",max_length=512)
	question = models.TextField(verbose_name="Pergunta")


	class Meta:
		verbose_name = "Forum"
		verbose_name_plural = "Foruns"

	def __str__(self):
		return self.name.encode("utf8")

	def save(self, *args, **kwargs):
		self.url = slugify(self.name.encode("utf8"))
		super(Forums, self).save(*args, **kwargs)


class Followers(models.Model):
	id = models.AutoField(verbose_name="Id",unique=True,primary_key=True)

	user = models.ForeignKey(Users,verbose_name="Usuários")
	forum = models.ForeignKey(Forums,verbose_name="Forum")

	class Meta:
		verbose_name = "Seguidor"
		verbose_name_plural = "Seguidores"

	def __str__(self):
		return self.forum.name.encode("utf8") + " - " + self.user.name.encode("utf8")

class Answers(models.Model):
	id = models.AutoField(verbose_name="Id",unique=True,primary_key=True)

	user = models.ForeignKey(Users,verbose_name="Usuário")
	forum = models.ForeignKey(Forums,verbose_name="Forum")
	message = models.TextField(verbose_name="Mensagem")

	class Meta:
		verbose_name = "Resposta"
		verbose_name_plural = "Respostas"

	def __str__(self):
		return self.forum.name.encode("utf8") + " - " + self.user.name.encode("utf8")


class Likes(models.Model):
	id = models.AutoField(verbose_name="Id",unique=True,primary_key=True)

	user = models.ForeignKey(Users,verbose_name="Usuário")
	answer = models.ForeignKey(Answers,verbose_name="Resposta")

	class Meta:
		verbose_name = "Like"
		verbose_name_plural = "Likes"

	def __str__(self):
		return self.user.name.encode("utf8")
