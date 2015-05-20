#!/usr/bin/env python
# -*- coding: utf-8 -*-

from webapp import models


def findUser(user):

	usersModel = models.Users
	usersFilter = usersModel.objects.filter(username=user)

	user = usersFilter if len(usersFilter) > 0 else usersModel.objects.filter(email=user)

	if len(user) > 0:
		user = user[0]
		return user
	else:
		return False


class ExtractUser(object):

	def __init__(self,userObject):
		self.username = userObject.username
		self.name = userObject.name
		self.surname = userObject.surname
		self.email = userObject.email
		self.points = userObject.points

	def addPoint(self,point):
		user = findUser(self.username)
		user.points = self.points + point
		user.save()

def getId(user):
	userModel = findUser(user)
	return userModel.id

def username(user):

	userModel = findUser(user)
	return userModel.username

def login(user,password):

	usersModel = findUser(user)

	if password == usersModel.password:
		return True
	else:
		return False

def get(user):
	userModel = findUser(user)

	return ExtractUser(userModel)
