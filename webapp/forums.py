from django.shortcuts import render_to_response,redirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from forum import users,ForumsList

def index(request):

	try:
		request.session['login'] == True
	except KeyError:
		request.session['login'] = False



	if not request.session['login']:
		return redirect("/forum/login")
	else:
		user = users.get(request.session['user'])
		c = {u"user" : user.username,u"forumsList": ForumsList.findUserForums(user.username)}
		c.update(csrf(request))
		return render_to_response("index.html",c)

def dashboard(request):

	try:
		request.session['login'] == True
	except KeyError:
		request.session['login'] = False



	if not request.session['login']:
		return redirect("/forum/login")
	else:
		user = users.get(request.session['user'])
		c = {u"user" : user.username,u"forumsList": ForumsList.findUserForums(user.username)}
		c.update(csrf(request))
		return render_to_response("forum/dashboard.html",c)

		

def loginView(request):
	if request.method == "GET":

		if request.session['login'] :
			return redirect("/forum/dashboard")
		else:
			c = {}
			c.update(csrf(request))
			return render_to_response("forum/login.html",c)

	elif request.method == "POST":

		user = request.POST.get("user",False)
		password = request.POST.get("password",False)

		if users.login(user,password):
			request.session['login'] = True
			request.session['user'] = users.username(user)

			
			return redirect("/forum/dashboard")
		else:

			c = {u"error" : True}
			c.update(csrf(request))
			return render_to_response("forum/login.html",c)

def logout(request):
	request.session['login'] = False
	request.session['user'] = ""
	return redirect("/forum/login")


def view(request,user,forum):

	return HttpResponse(user + "<br>" + forum)