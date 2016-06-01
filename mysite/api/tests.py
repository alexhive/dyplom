"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase, Client
import models, json

class UserDataTest(TestCase):
    def setUp(self):
        models.Userdata.objects.create(user_id=1, name="Sum", region_id=1, address="Sum", person="Marc")

    def test_Get_Userdata(self):
        c = Client()
        response = c.get("/api/user/?name=Sum")
        self.assertEqual(json.loads(response.content),  [{
                        "user_id": "1",
                        "name": "Sum",
                        "region_id": "1",
                        "address": "Sum",
                        "person": "Marc"
                    }])

    def test_Get_Userdata_fail(self):
        c = Client()
        response = c.get("/api/user/?name=Num")
        self.assertEqual(json.loads(response.content), [])


class PurchaseDataTest(TestCase):
    def setUp(self):
        user = models.Userdata.objects.create(user_id=1, name="Sum", region_id=1, address="Sum", person="Marc")
        models.Purchase.objects.create(purchase_id=1, user=user, announce_id=1, goods_name="Nail")

    def test_Get_Purchase(self):
        c = Client()
        response = c.get("/api/purchase/?name=Nail")
        self.assertEqual(json.loads(response.content),  [{
                        "purchase_id": "1",
                        "user": 1.0,
                        "announce_id": "1"
                    }])

    def test_Get_Purchase_fail(self):
        c = Client()
        response = c.get("/api/purchase/?name=Naive")
        self.assertEqual(json.loads(response.content), [])


class WinnerDataTest(TestCase):
    def setUp(self):
        user = models.Userdata.objects.create(user_id=1, name="Sum", region_id=1, address="Sum", person="Marc")
        purchase = models.Purchase.objects.create(purchase_id=1, user=user, announce_id=1, goods_name="Nail")
        models.Winner.objects.create(winner_id=1, winner_name="Sally", purchase=purchase, winner_address="Kolombo", w_id=100)

    def test_Get_Winner(self):
        c = Client()
        response = c.get("/api/winner/?name=Sally")
        self.assertEqual(json.loads(response.content), [{
            "purchase": 1.0,
            "winner_name": "Sally",
            "winner_address": "Kolombo",
            "winner_id": "1",
            "w_id": 100
        }])

    def test_Get_Winner_fail(self):
        c = Client()
        response = c.get("/api/winner/?name=Sails")
        self.assertEqual(json.loads(response.content), [])
