#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.signing import Signer
from webapp import models

class Security(object):

	def __init__(self,request,users):
		self.users = users
		self.request = request

	def check(self):
		try:
			self.request.session['login'] == True
		except KeyError:
			self.request.session['login'] = False

		return self.request.session['login']

	def islogged(self):
		
		self.check()
		return self.request.session['login']

	def login(self,user,password):
		
		usersModel = self.users.find(user)
		if password == usersModel.password:
			self.request.session['login'] = True
			self.request.session['user'] = self.users.username(user)
			return True
		else:
			return False


	def logout(self):
		request.session['login'] = False
		request.session['user'] = "" 

	def register(self,username,firstName,surName,email,password):
		pass