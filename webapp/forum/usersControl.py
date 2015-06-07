#!/usr/bin/env python
# -*- coding: utf-8 -*-

from webapp import models

class users(object):

	def __init__(self,request):
		self.request = request


	def find(self,user):

		usersModel = models.Users
		usersFilter = usersModel.objects.filter(username=user)

		user = usersFilter if len(usersFilter) > 0 else usersModel.objects.filter(email=user)

		if len(user) > 0:
			user = user[0]
			return user
		else:
			return False

	def username(self,user):

		userModel = self.find(user)
		return userModel.username

	def logged(self):
		loggedUser = self.request.session['user']
		user_id = id(loggedUser)
		loggedUser = self.username(loggedUser)
		loggedUser = self.get(loggedUser)

		return loggedUser

	def id(self,user):
		userModel = self.find(user)
		if userModel == False:
			return False
		else:
			return userModel.id

	def get(self,user):
		userModel = self.find(user)
		return self.ExtractUser(userModel,self.find)

	class ExtractUser(object):

		def __init__(self,userObject,find):
			self.username = userObject.username
			self.name = userObject.name
			self.surname = userObject.surname
			self.email = userObject.email
			self.points = userObject.points
			self.__find = find

		def addPoint(self,point):
			user = self.__find(self.username)
			user.points = self.points + point
			user.save()
