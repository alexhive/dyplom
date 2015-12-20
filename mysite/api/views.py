from serializers import *
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import mysite.models as models
import serializers
import json
from utils import Pointer

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
		if obj == p.object:
			return p.position

	return -1

def getd3jsjsonForUser( userdata_list, purchase_list, w_list ):
	response = { "nodes" : [], "links" : [] }
	pointers = []

	if 0 != len(userdata_list):
		response["nodes"].append( {"atom": userdata_list[0].name, "size": 30} )

	for node in purchase_list:
		response["links"].append( { "bond" : 1, "source" : len(response["nodes"]), "target" : 0 } )
		response["nodes"].append( {"atom": node.goods_name, "size": 15} )

	for node in w_list:
		pos = findPoint(node.winner_name, pointers)
		if -1 == pos:
			pos = len(response["nodes"])
			response["nodes"].append( {"atom": node.winner_name, "size": 5} )
			
			pointers.append( Pointer( node.winner_name, pos ) )

		response["links"].append( { "bond" : 1, "source" : len(userdata_list) + purchase_list.index(node.purchase), "target" : pos } )
		
	return response


def getd3jsjsonForWinner( userdata_list, purchase_list, w_list ):
	response = { "nodes" : [], "links" : [] }
	pointers = []

	if 0 != len(w_list):
		response["nodes"].append( {"atom": w_list[0].winner_name, "size": 30} )
	else:
		return response

	for node in w_list:
		w_pos = len(response["nodes"])
		myName = node.purchase.goods_name
		if None == myName:
			myName = ""
		response["nodes"].append( {"atom": myName, "size": 3} )
		response["links"].append( { "bond" : 1, "source" : 0, "target" : w_pos } )
		pos = findPoint(node.purchase.user, pointers)
		if -1 == pos:
			response["nodes"].append( {"atom": node.purchase.user.name, "size": 30} )
			pos = w_pos + 1
			pointers.append( Pointer( node.purchase.user, pos ) )
		response["links"].append( { "bond" : 1, "source" : w_pos,  "target" : pos } )

	return response


@api_view(['GET',])
def UserdataToWinner(req):
	userdata_id = [ x.user_id for x in list(models.Userdata.objects.filter( name = req.GET["name"] )) ]
	userdata_id_parent_sort = [ x.parent_id for x in list( models.UserdataSort.objects.filter( id__in = userdata_id ) ) ]
	userdata_id_sort = [ x.id for x in list( models.UserdataSort.objects.filter( parent_id__in = userdata_id_parent_sort ) ) ]
	print("userdata_id", len(userdata_id))
	print("userdata_id_parent_sort", len(userdata_id_parent_sort))
	print("userdata_id_sort", len(userdata_id_sort))

	# get purchase with name
	userdata_list = list(models.Userdata.objects.filter( user_id__in = userdata_id_sort ))
	print "list objects user count {0}".format(len(userdata_list))

	# get purchase with name
	purchase_list = list(models.Purchase.objects.filter( user__in = userdata_list ))
	print "list objects purchase count {0}".format(len(purchase_list))

	# get winners with purchase
	w_list = list(models.Winner.objects.filter( purchase__in = purchase_list ))
	print "list objects winners count {0}".format(len(w_list))

	return HttpResponse(json.dumps(getd3jsjsonForUser( userdata_list, purchase_list, w_list )), content_type="application/json")

@api_view(['GET',])
def WinnerToUser(req):
	print(req.GET["name"], len(req.GET["name"]))
	
	winner_id = [ x.winner_id for x in list(models.Winner.objects.filter( winner_name = req.GET["name"] )) ]
	winner_id_parent_sort = [ x.parent_id for x in list( models.WinnerSort.objects.filter( id__in = winner_id ) ) ]
	winner_id_sort = [ x.id for x in list( models.WinnerSort.objects.filter( parent_id__in = winner_id_parent_sort ) ) ]
	print("winner_id = ", len(winner_id))
	print("winner_id_parent_sort", len(winner_id_parent_sort))
	print("winner_id_sort", len(winner_id_sort))

	# get winners with purchase
	w_list = list(models.Winner.objects.filter( winner_id__in = winner_id_sort ))
	print "list objects winners count {0}".format(len(w_list))

	purchase_list = []
	for node in w_list:
		if None != node.purchase:
			purchase_list.append( node.purchase )
	print "list objects purchase count {0}".format(len(w_list))

	userdata_list = []
	for node in purchase_list:
		if None != node.user:
			userdata_list.append( node.user )
	print "list objects user count {0}".format(len(userdata_list))

	return HttpResponse(json.dumps(getd3jsjsonForWinner( userdata_list, purchase_list, w_list )), content_type="application/json")