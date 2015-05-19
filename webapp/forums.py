from django.shortcuts import render_to_response,redirect
from django.http import HttpResponse


def index(request):

	try:
		request.session['login'] == True
	except KeyError:
		request.session['login'] = False



	if not request.session['login']:
		return redirect("/forum/login")
	else:
		return render_to_response("index.html")

		

def login(request):
	if request.session['login'] :
		return redirect("/forum")
	else:
		return render_to_response("forum/login.html")