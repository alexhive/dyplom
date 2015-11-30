# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext

import froms
import mysite.models as models

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def returnForUserD3JS(request):
	print(request.GET["name"])
	link = "http://127.0.0.1:8000/api/userToWinner/?name=" + request.GET["name"]
	print("link = ", link)
	print("name = ", request.GET["name"])
	return render(request, "grap_sample.html", {
		'url' : link,
		}, context_instance=RequestContext(request))

def returnForwinnerD3JS(request):
	link = "http://127.0.0.1:8000/api/winnerToUser/?name=" + request.GET["name"]
	print(request.GET["name"])
	print("link = ", link)
	return render(request, "grap_sample.html", {
		'url' : link,
		}, context_instance=RequestContext(request))

def GraphicRequest(request):
	print "metod: ", request.method
	if "GET" == request.method:
		return render(request, 'name.html', {'form': froms.NameForm()})
	elif "POST" == request.method:
		
		# get user list with name
		l = models.Userdata.objects.filter( name = request.POST["name"] )
		print "list objects user count {0}".format(len(l))

		# get purchase with name
		purchase_list = models.Purchase.objects.filter( user__in = l )
		print "list objects purchase count {0}".format(len(purchase_list))

		# get winners with purchase
		w_list = models.Winner.objects.filter( purchase__in = purchase_list )
		print "list objects winners count {0}".format(len(w_list))

		return redirect('graph')

	return HttpResponse("!!!")