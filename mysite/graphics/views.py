# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django import forms

import mysite.models as models

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")
 
class PostForm(forms.Form):
    user = forms.CharField(max_length=256)
    year = forms.IntegerField()
    winner = forms.CharField(max_length=256)

    def __init__(self, user = "", year = 2015, winner = "", *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["user"].initial = user
        self.fields["winner"].initial = winner

def returnForUserD3JS(request):
	print "metod: ", request.method
	if "GET" == request.method:
		return render(request, "grap_sample.html", {
			'from' : PostForm(),
			}, context_instance=RequestContext(request))
	else:
		print(request.POST["name"])
		link = "http://127.0.0.1:8000/api/userToWinner/?name=" + request.POST["name"]
		print("link = ", link)
		print("name = ", request.POST["name"])
		return render(request, "grap_sample.html", {
			'url' : link,
			}, context_instance=RequestContext(request))


def returnForwinnerD3JS(request):
	link = "http://127.0.0.1:8000/api/winnerToUser/?name=" + request.GET["name"]
	print(request.GET["name"], len(request.GET["name"]))
	print link
	return render(request, "grap_sample.html", {
		'url' : link,
		}, context_instance=RequestContext(request))

def GraphicRequest(request):
	print "metod: ", request.method
	if "GET" == request.method:
		return render(request, 'grap_sample.html', {'form': PostForm})
	elif "POST" == request.method:
		winnerName =  request.POST["winner"]
		userName = request.POST["user"]
		year = request.POST["year"]

		link = ""
		if "" != winnerName and "" == userName:
			link = "http://127.0.0.1:8000/api/winnerToUser/?name=" + winnerName
		elif "" == winnerName and "" != userName:
			link = "http://127.0.0.1:8000/api/userToWinner/?name=" + userName
		elif "" != winnerName and "" != userName:
			link = u"http://127.0.0.1:8000/api/winnerToConcreteUser/?user={0}&winner={1}".format(userName, winnerName)

		form = PostForm(user = userName, winner = winnerName)
		return render(request, 'grap_sample.html', {'form': form, 'url': link})

	return HttpResponse("!!!")