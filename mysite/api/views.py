from serializers import *
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import mysite.models as models
import serializers
import json


@api_view(['GET',])
def RESTUser(req):
	"""
	List all bti, or create a new bti.
	"""
	if req.method == 'GET':
		print "user request"

		user_all = models.Userdata.objects.filter( name = req.GET["name"] )
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

@api_view(['GET',])
def UserdataToWinner(req):
	response = { "nodes" : [], "links" : [] }

	# get user list with name
	l = models.Userdata.objects.filter( name = req.GET["name"] )

	if 0 == len(l):
		return HttpResponse(json.dumps(response), content_type="application/json")

	user_obj_id = l[0].user_id
	parent_object = models.UserdataSort.objects.filter( userdata_id = user_obj_id )
	parent_object_id = parent_object[0].parent_id

	same_objects = models.UserdataSort.objects.filter( parent_id = parent_object_id )
	same_objects_id = []
	for o in same_objects:
		same_objects_id.append(o.id)

	print "list objects user count {0}".format(len(l))

	# get purchase with name
	purchase_list = models.Purchase.objects.filter( user__in = same_objects_id )
	print "list objects purchase count {0}".format(len(purchase_list))

	# get winners with purchase
	w_list = models.Winner.objects.filter( purchase__in = purchase_list )
	print "list objects winners count {0}".format(len(w_list))

	
	for node in l:
		response["nodes"].append( {"atom": node.name, "size": 20} )

	for node in purchase_list:
		response["nodes"].append( {"atom": node.goods_name, "size": 10} )

	for node in w_list:
		response["nodes"].append( {"atom": node.winner_name, "size": 5} )

	return HttpResponse(json.dumps(response), content_type="application/json")