from rest_framework import serializers
import mysite.models as models
from django.forms import widgets
import mysite.models as models

class UserdataSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Userdata
		fields = ('user_id', "name", "region_id", "address", "person")


class PurchaseSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Purchase
		fields = ('purchase_id', "user", "announce_id")

class WinnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Winner
		fields = ('winner_id', "purchase", "winner_name", "winner_address", "w_id")