from django.shortcuts import render_to_response,redirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from forum import usersControl,ForumsList
from security import securityControl
from webapp import models

def isNotEmpty(s):
    return bool(s and s.strip())

def reply(request,user,forum):
	
	users = usersControl.users(request)
	security = securityControl.Security(request,users)
	if request.method == "POST":

		if security.islogged():
			answer = request.POST.get("answer",False)
			loggedUser = users.logged()
			loggedUser_id = users.id(loggedUser.username)
			forum_id = ForumsList.forumId(forum,user)

			if not answer == False and isNotEmpty(answer):
				
				answers = models.Answers(user_id=loggedUser_id,forum_id=forum_id,message=answer)
				answers.save()
				loggedUser.addPoint(5)

			return redirect("/forum/" + user + "/" + forum)
		else:
			render_to_response("forum/404.html")
		
	else:
		render_to_response("forum/404.html")

def like(request,user,forum,answer):
	
	users = usersControl.users(request)
	security = securityControl.Security(request,users)

	if security.islogged():
	
		loggedUser = users.logged()
		user_id = users.id(loggedUser.username)
		likesModel = models.Likes
		likes = likesModel.objects.filter(user_id=user_id, answer_id=answer)

		if len(likes) == 0:
			like = models.Likes(user_id=user_id,answer_id=answer)
			like.save()

		return redirect("/forum/" + user + "/" + forum)

	else:
		render_to_response("forum/404.html")

def unlike(request,user,forum,answer):

	users = usersControl.users(request)
	security = securityControl.Security(request,users)

	if security.islogged():

		loggedUser = users.logged()
		loggedUser_id = users.id(loggedUser.username)
		likesModel = models.Likes
		likes = likesModel.objects.filter(user_id=loggedUser_id, answer_id=answer)
		likes[0].delete()

		return redirect("/forum/" + user + "/" + forum)

	else:
		render_to_response("forum/404.html")
