#!/usr/bin/env python
# -*- coding: utf-8 -*-

from webapp import models
from . import usersControl


class forums(object):

	def __init__(self,request,users):
		self.users = users
		self.sessionUser = self.users.logged()
		self.model = models.Forums
		self.request = request

	class details(object):

		def __init__(self, name, creator, description, question,replies, url):
			self.name = name
			self.creator = creator
			self.description = description
			self.question = question
			self.replies = replies
			self.repliesLength = len(replies)
			self.url = url
			self.id = id
	
	class replyConstructor(object):
		
		def __init__(self, user, message, likes,id,currentUser,iliked,users):
			self.user = user
			self.id = id
			self.message = message
			self.likes = likes
			self.likesLength = len(self.likes)
			self.iliked = iliked(self.id,users.id(currentUser.username))

	def iliked(self,answer_id,user_id):
			
		likesModel = models.Likes
		likes = likesModel.objects.filter(user_id=user_id,answer_id=answer_id)
		if len(likes) > 0:
			return True

		return False

	def likes(self,answer):
		likesModel = models.Likes
		likes = likesModel.objects.filter(answer_id=answer.id)

		likesList = []

		for like in likes:
			user = self.users.username(like.user.username)
			user = self.users.get(user)
			likesList.append(user)

		return likesList

	def followers(self,forum):
		
		followersModel = models.Followers
		followers = followersModel.objects.filter(forum_id=forum.id)

		followersData = []

		for follower in followers:
			user = users.get(users.user.username)
			followersData.append(user)

		return followersData

	def following(self,user):
		
		user_id = self.users.id(user)
		followersModel = models.Followers
		followers = followersModel.objects.filter(user_id=user_id)

		followersData = []

		for follower in followers:
			followersData.append(self.get(follower.forum.id))

		return followersData

	def replies(self,forum):
		AnswersModel = models.Answers
		answers = AnswersModel.objects.filter(forum_id=forum.id)

		replies = []

		for answer in answers:
			user = self.users.get(answer.user.username)
			likes = self.likes(answer)
			replies.append(self.replyConstructor(user,answer.message,likes,answer.id,self.users.logged(),self.iliked,self.users))

		return replies

	def get(self,id):

		forumsModel = models.Forums
		forum = forumsModel.objects.filter(id=id)[0]
		user = self.users.get(forum.creator.username)
		replies = self.replies(forum)
		return self.details(forum.name,user,forum.descriptions, forum.question,replies,forum.url)

	def list(self,user):
		
		user_id = self.users.id(user)
		user = self.users.get(user)

		forums = self.model.objects.filter(creator_id=user_id)

		usersForum = []

		for forum in forums:
			replies = self.replies(forum)
			details = self.details(forum.name,user,forum.descriptions, forum.question,replies,forum.url)
			usersForum.append(details)

		return usersForum

	def id(self,url,user):
		user_id = users.getId(user)
		forumsModel = models.Forums
		forum = forumsModel.objects.filter(creator_id=user_id,url=url)[0]
		return forum.id

	def find(self,url,user):
		user_id = self.users.id(user)
		if not user_id == False:
			user = self.users.get(user)

			forumsModel = models.Forums
			forum = forumsModel.objects.filter(creator_id=user_id,url=url)[0]
			replies = self.replies(forum)
			return self.details(forum.name,user,forum.descriptions, forum.question,replies,forum.url)
		else:
			return False
