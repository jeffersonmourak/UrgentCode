from django.shortcuts import render_to_response,redirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from forum import usersControl,forumsControl
from security import securityControl
from webapp import models

def index(request):

	users = usersControl.users(request)
	forums = forumsControl.forums(request,users)

	if not security.islogged(request):
		return redirect("/forum/login")
	else:
		user = users.get(request.session['user'])
		pageData = {u"user" : user.username,u"forumsList": forums.list(user.username)}
		pageData.update(csrf(request))
		return render_to_response("index.html",pageData)

def dashboard(request):

	
	users = usersControl.users(request)
	forums = forumsControl.forums(request,users)
	security = securityControl.Security(request,users)

	if not security.islogged():
		return redirect("/forum/login")
	else:
		loggedUser = users.logged()

		

		user = users.get(request.session['user'])
		pageData = {
			u"user" : user.username,
			u"forumsList": forums.list(user.username),
			u"following": forums.following(request.session['user'])
		}
		pageData.update(csrf(request))
		return render_to_response("forum/dashboard.html",pageData)

def loginView(request):

	users = usersControl.users(request)
	security = securityControl.Security(request,users)

	if request.method == "GET":
		if security.islogged():
			return redirect("/forum/dashboard")
		else:
			pageData = {}
			pageData.update(csrf(request))
			return render_to_response("forum/login.html",pageData)

	elif request.method == "POST":

		user = request.POST.get("user",False)
		password = request.POST.get("password",False)

		if security.login(user,password):
			return redirect("/forum/dashboard")
		else:
			pageData = {u"error" : True}
			pageData.update(csrf(request))
			return render_to_response("forum/login.html",pageData)

def logout(request):

	users = usersControl.users(request)
	security = securityControl.Security(request,users)
	security.logout()
	return redirect("/forum/login")

def view(request,user,forum):

	users = usersControl.users(request)
	forums = forumsControl.forums(request,users)

	if request.method == "GET":

		loggedUser = users.logged()

		forumData = forums.find(forum,user)

		if forumData == False:
			return render_to_response("forum/404.html")

		else:
			loggedUser = request.session['user']

			user_id = users.id(loggedUser)
			loggedUser = users.username(loggedUser)
			loggedUser = users.get(loggedUser)

			pageData = { 
				"forum" : forumData,
				"user" : loggedUser,
				"user_id" : user_id,
			}
			pageData.update(csrf(request))
			return render_to_response("forum/forum.html",pageData)
