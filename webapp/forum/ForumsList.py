#!/usr/bin/env python
# -*- coding: utf-8 -*-

from webapp import models
from . import users


class ForumDetails(object):

	def __init__(self, name, creator, description, question,replies):
		self.name = name
		self.creator = creator
		self.description = description
		self.question = question
		self.replies = replies
		self.repliesLength = len(replies)
		


class ReplyDetails(object):
	
	def __init__(self, user, message, likes):
		self.user = user
		self.message = message
		self.likes = likes
		

def getLikes(answer):
	likesModel = models.Likes
	likes = likesModel.objects.filter(answer_id=answer.id)

	likesList = []

	for like in likes:
		user = users.username(like.user.username)
		user = users.get(user)
		likesList.append(user)

	return likesList





def getForumReplies(forum):
	AnswersModel = models.Answers
	answers = AnswersModel.objects.filter(forum_id=forum.id)

	replies = []

	for answer in answers:
		user = users.username(answer.user.username)
		user = users.get(user)
		likes = getLikes(answer)
		replies.append(ReplyDetails(user,answer.message,likes))

	return replies

def findUserForums(user):
	
	user_id = users.getId(user)
	user = users.username(user)
	user = users.get(user)

	forumsModel = models.Forums
	forumsFilter = forumsModel.objects.filter(creator_id=user_id)

	forumsList = []

	for forum in forumsFilter:
		replies = getForumReplies(forum)
		forumClass = ForumDetails(forum.name,user,forum.descriptions, forum.question,replies)
		forumsList.append(forumClass)

	return forumsList