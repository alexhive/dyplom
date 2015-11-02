# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404, render

import froms

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def GraphicRequest(request):
	print "metod: ", request.method
	if "GET" == request.method:
		return render(request, 'name.html', {'form': froms.NameForm()})
	elif "POST" == request.method:
		
		return HttpResponse("post method")

	return HttpResponse("!!!")