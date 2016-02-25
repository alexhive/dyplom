from serializers import *
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import mysite.models as models
import serializers
import json
import tempfile
import os
from utils import Pointer

AUTOCOMPLETE_LIMIT = 10

@api_view(['GET',])
def RESTUser(req):
	"""
	List all bti, or create a new bti.
	"""
	if req.method == 'GET':
		print "user request"

		user_all = models.Userdata.objects.filter( name = req.GET["name"] )#like!!!!#
		res = []

		for obj in user_all:
			res.append( UserdataSerializer(obj).data )

		return Response(res)

@api_view(['GET',])
def RESTPurchase(req):
	"""
	List all bti, or create a new bti.
	"""
	if req.method == 'GET':
		print "user request"

		purchase_all = models.Purchase.objects.filter( goods_name = req.GET["name"] )
		res = []

		for obj in purchase_all:
			res.append( PurchaseSerializer(obj).data )

		return Response(res)


@api_view(['GET',])
def RESTWinner(req):
	"""
	List all bti, or create a new bti.
	"""
	if req.method == 'GET':
		print "user request"

		winner_all = models.Winner.objects.filter( winner_name = req.GET["name"] )
		res = []

		for obj in winner_all:
			res.append( WinnerSerializer(obj).data )

		return Response(res)

def findPoint(obj, pointers):
	for p in pointers:
		if obj == p["atom"]:
			return pointers.index(p)

	return -1

def ceateResponse(winner_list):
	response = { "nodes" : [], "links" : [] }
	winnerForTable = []

	for node in winner_list:
		posWinner = findPoint(node.winner_name, response["nodes"])
		if -1 == posWinner:
			winnerForTable.append(node)
			posWinner = len(response["nodes"])
			response["nodes"].append( {"atom": node.winner_name, "size": 30, "color" : "#0000ff"} )

		posPurchase = findPoint(node.purchase.goods_name, response["nodes"])
		if -1 == posPurchase:
			posPurchase = len(response["nodes"])
			response["nodes"].append( {"atom": node.purchase.goods_name, "size": 20, "color" : "#00ff00"} )

		posUserdata = findPoint(node.purchase.user.name, response["nodes"])
		if -1 == posUserdata:
			posUserdata = len(response["nodes"])
			response["nodes"].append( {"atom": node.purchase.user.name, "size": 10, "color" : "#ff0000"} )

		response["links"].append( { "bond" : 1, "source" : posWinner,  "target" : posPurchase } )
		response["links"].append( { "bond" : 1, "source" : posPurchase,  "target" : posUserdata } )

	response["table_file"] = saveWinnerTable(winnerForTable)
	return response


def suitableYear(year, purchaseYear):
	if None == year:
		return True

	if None == purchaseYear:
		return False

	print(year, purchaseYear)
	print("purchase year = ", purchaseYear.year)
	if year == purchaseYear.year:
		return True
	else:
		return False

@api_view(['GET',])
def UserdataToWinner(req):
	try:
		year = int(req.GET["year"]) if "year" in req.GET.keys() else None
	except:
		year = None
	print("YEAR = ", year)

	userdata_id = [ x.user_id for x in list(models.Userdata.objects.filter( name__icontains = req.GET["name"] )) ]
	userdata_id_parent_sort = [ x.parent_id for x in list( models.UserdataSort.objects.filter( id__in = userdata_id ) ) ]
	userdata_id_sort = [ x.id for x in list( models.UserdataSort.objects.filter( parent_id__in = userdata_id_parent_sort ) ) ]
	print("userdata_id", len(userdata_id))
	print("userdata_id_parent_sort", len(userdata_id_parent_sort))
	print("userdata_id_sort", len(userdata_id_sort))

	# get purchase with name
	u_list = list(models.Userdata.objects.filter( user_id__in = userdata_id_sort ))
	print "list objects user count {0}".format(len(u_list))

	# get purchase with name
	p_list = list(models.Purchase.objects.filter( user__in = u_list ))
	print "list objects purchase count {0}".format(len(p_list))

	# get winners with purchase
	w_list = list(models.Winner.objects.filter( purchase__in = p_list ))
	print "list objects winners count {0}".format(len(w_list))

	winner_list = []
	for node in w_list:
		if None != node.purchase:
			if suitableYear(year, node.purchase.purchase_publicated):
				if None != node.purchase.user:
					winner_list.append( node )

	return HttpResponse(json.dumps(ceateResponse( winner_list )), content_type="application/json")

@api_view(['GET',])
def WinnerToUser(req):
	print(req.GET["name"], len(req.GET["name"]))
	try:
		year = int(req.GET["year"]) if "year" in req.GET.keys() else None
	except:
		year = None
	print("YEAR = ", year)
	
	winner_id = [ x.winner_id for x in list(models.Winner.objects.filter( winner_name__icontains = req.GET["name"] )) ]
	winner_id_parent_sort = [ x.parent_id for x in list( models.WinnerSort.objects.filter( id__in = winner_id ) ) ]
	winner_id_sort = [ x.id for x in list( models.WinnerSort.objects.filter( parent_id__in = winner_id_parent_sort ) ) ]
	print("winner_id = ", len(winner_id))
	print("winner_id_parent_sort", len(winner_id_parent_sort))
	print("winner_id_sort", len(winner_id_sort))

	# get winners with purchase
	w_list = list(models.Winner.objects.filter( winner_id__in = winner_id_sort ))
	print "list objects winners count {0}".format(len(w_list))

	winner_list = []
	for node in w_list:
		if None != node.purchase:
			if suitableYear(year, node.purchase.purchase_publicated):
				if None != node.purchase.user:
					winner_list.append( node )

	return HttpResponse(json.dumps(ceateResponse( winner_list )), content_type="application/json")

@api_view(['GET',])
def WinnerToConcreteUser(req):
	try:
		year = int(req.GET["year"]) if "year" in req.GET.keys() else None
	except:
		year = None
	print("YEAR = ", year)
	winer_name = req.GET["winner"]
	user_name = req.GET["user"]
	
	winner_id = [ x.winner_id for x in list(models.Winner.objects.filter( winner_name__icontains = winer_name )) ]
	winner_id_parent_sort = [ x.parent_id for x in list( models.WinnerSort.objects.filter( id__in = winner_id ) ) ]
	winner_id_sort = [ x.id for x in list( models.WinnerSort.objects.filter( parent_id__in = winner_id_parent_sort ) ) ]
	print("winner_id = ", len(winner_id))
	print("winner_id_parent_sort", len(winner_id_parent_sort))
	print("winner_id_sort", len(winner_id_sort))

	# get winners with purchase
	w_list = list(models.Winner.objects.filter( winner_id__in = winner_id_sort ))
	print "list objects winners count {0}".format(len(w_list))

	winner_list = []
	for node in w_list:
		if None != node.purchase:
			if suitableYear(year, node.purchase.purchase_publicated):
				if None != node.purchase.user:
					if user_name in node.purchase.user.name:
						winner_list.append( node )

	return HttpResponse(json.dumps(ceateResponse( winner_list )), content_type="application/json")

@api_view(['GET',])
def UserAutocomplete(req):
	print("Autocomplete", req.GET["name"])
	if "" == req.GET["name"]:
		return HttpResponse(json.dumps({}), content_type="application/json")	
	
	query = u"select distinct on (name) name, user_id from userdata where LOWER( name ) like '%%{0}%%' limit {1};".format(req.GET["name"].lower(), AUTOCOMPLETE_LIMIT)
	print(query)
	res_list = [ x.name for x in list(models.Userdata.objects.raw(query)) ]
	return HttpResponse(json.dumps(res_list), content_type="application/json")	

@api_view(['GET',])
def WinnerAutocomplete(req):
	if "" == req.GET["name"]:
		return HttpResponse(json.dumps({}), content_type="application/json")
		
	query = u"select distinct on (winner_name) winner_name, winner_id from winner where LOWER( winner_name ) like '%%{0}%%' limit {1};".format(req.GET["name"].lower(), AUTOCOMPLETE_LIMIT)
	print(query)

	db_list = [ x.winner_name for x in list(models.Winner.objects.raw(query)) ]
	res_list = []
	for obj in db_list:
		res_list.append( { "label" : obj, "value" : obj } )

	print(res_list)
	return HttpResponse(json.dumps(res_list), content_type="application/json")	

def saveWinnerTable(winnerList):
	res = []
	for obj in winnerList:
		arr = []
		arr.append(obj.winner_name)
		arr.append(obj.winner_code)
		arr.append(obj.winner_phone)
		arr.append(obj.winner_address)
		res.append(arr)


	f = tempfile.NamedTemporaryFile("wb", delete = False)
	# f.write(res.encode('utf8'))
	f.write( json.dumps({"data" : res}) )
	name = f.name
	f.close()

	return name

@api_view(['GET',])
def getWinnerTable(req):
	file_name = req.GET["name"]

	try:
		f = open(file_name, "r")
		content = f.read()
		f.close()
		os.remove(file_name)
		return HttpResponse(content, content_type="html")
	except:
		print("Error ocqurence with file %s" % file_name)

	return 	HttpResponse("Something went wrong", content_type="application/json")