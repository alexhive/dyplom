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


class GraphTests(TestCase):
    def setUp(self):
        user = models.Userdata.objects.create(user_id=1, name="Sum", region_id=1, address="Sum", person="Marc")
        models.UserdataSort.objects.create(id=1, parent_id=1, name="Sum")
        purchase = models.Purchase.objects.create(purchase_id=1, user=user, announce_id=1, goods_name="Nail")
        models.Winner.objects.create(winner_id=1, winner_name="Sally", purchase=purchase, winner_address="Kolombo", w_id=100)
        models.WinnerSort.objects.create(id=1, parent_id=1, name="Sally")

    def test_logic_graphFromName(self):
        c = Client()
        response = c.get("/api/graph_from_name/?name=Sum")

        body = json.loads(response.content)
        body.pop("table_file")
        self.assertEqual({u'links': [{u'bond': 1, u'source': 0, u'target': 1},
                                        {u'bond': 1, u'source': 1, u'target': 2}],
                        u'nodes': [{u'atom': u'Sally', u'color': u'#0000ff', u'size': 30},
                                    {u'atom': u'Nail', u'color': u'#00ff00', u'size': 20},
                                    {u'atom': u'Sum', u'color': u'#ff0000', u'size': 10}]},
                         body)

    def test_logic_WinnerToUser(self):
        c = Client()
        response = c.get("/api/winnerToUser/?name=Sally")

        body = json.loads(response.content)
        body.pop("table_file")
        self.assertEqual({u'links': [{u'bond': 1, u'source': 0, u'target': 1},
                                        {u'bond': 1, u'source': 1, u'target': 2}],
                        u'nodes': [{u'atom': u'Sally', u'color': u'#0000ff', u'size': 30},
                                    {u'atom': u'Nail', u'color': u'#00ff00', u'size': 20},
                                    {u'atom': u'Sum', u'color': u'#ff0000', u'size': 10}]},
                         body)

    def test_logic_WinnerToConcreteUser(self):
        c = Client()
        response = c.get("/api/winnerToConcreteUser/?winner=Sally&user=Sum")

        body = json.loads(response.content)
        body.pop("table_file")
        self.assertEqual({u'links': [{u'bond': 1, u'source': 0, u'target': 1},
                                     {u'bond': 1, u'source': 1, u'target': 2}],
                          u'nodes': [{u'atom': u'Sally', u'color': u'#0000ff', u'size': 30},
                                     {u'atom': u'Nail', u'color': u'#00ff00', u'size': 20},
                                     {u'atom': u'Sum', u'color': u'#ff0000', u'size': 10}]},
                         body)

    def test_bunch_tmp_file_is_exist(self):
        def test_is_tmp_file(addres):
            c = Client()
            response = c.get(addres)
            body = json.loads(response.content)
            tmp = None
            tmp = body.pop("table_file")
            if tmp:
                return True
            else:
                return False

        addresses = ["/api/graph_from_name/?name=Sum",
                         "/api/userToWinner/?name=Sum",
                         "/api/winnerToUser/?name=Sally",
                         "/api/winnerToConcreteUser/?winner=Sally&user=Sum"]
        for add in addresses:
           if not test_is_tmp_file(add):
               self.assertFalse(add, "file not exist")

        return self.assertTrue(addresses, "file exists")

    def test_bunch_graph_unity(self):
        def test_graph_unity(addres):
            c = Client()
            response = c.get(addres)
            body = json.loads(response.content)
            body.pop("table_file")

            node_list = [False for x in range(len(body["nodes"]))]
            for link in body["links"]:
                if body["nodes"][link["source"]] and body["nodes"][link["target"]]:
                    node_list[link["source"]] = True
                    node_list[link["target"]] = True

            for x in node_list:
                if not x:
                    return False
            return True

        addresses = ["/api/graph_from_name/?name=Sum",
                     "/api/userToWinner/?name=Sum",
                     "/api/winnerToUser/?name=Sally",
                     "/api/winnerToConcreteUser/?winner=Sally&user=Sum"]

        for add in addresses:
            if not test_graph_unity(add):
                self.assertFalse(add, "graph is not unity")

        return self.assertTrue(addresses, "graph is unity")

class UserAutoComplete(TestCase):
    def setUp(self):
        models.Userdata.objects.create(user_id=1, name="Sum", region_id=1, address="Sum", person="Marc")
        models.Userdata.objects.create(user_id=2, name="Al", region_id=1, address="Sum", person="Marc")
        models.Userdata.objects.create(user_id=3, name="WeyHo", region_id=4, address="Sum", person="Marc")
        models.Userdata.objects.create(user_id=4, name="Bleze", region_id=4, address="Sum", person="Marc")
        models.Userdata.objects.create(user_id=5, name="Loem", region_id=1, address="Sum", person="Marc")
        models.Userdata.objects.create(user_id=6, name="Ipsum", region_id=67, address="Sum", person="Marc")
        models.Userdata.objects.create(user_id=7, name="Summmy", region_id=78, address="Sum", person="Marc")
        models.Userdata.objects.create(user_id=8, name="Summmer", region_id=16, address="Sum", person="Marc")
        models.Userdata.objects.create(user_id=9, name="Ipsum", region_id=90, address="Sum", person="Marc")
        models.Userdata.objects.create(user_id=10, name="casum", region_id=1, address="Sum", person="Marc")
        models.Userdata.objects.create(user_id=11, name="SUM", region_id=1, address="Sum", person="Marc")
        models.Userdata.objects.create(user_id=12, name="UPSUMLY", region_id=1, address="Sum", person="Marc")

    def test_UserAutocomplete(self):
        c = Client()
        response = c.get("/api/userAutocomplete/?name=Sum")

        self.assertEqual(json.loads(response.content),
                         [u'casum', u'Ipsum', u'Sum', u'SUM', u'Summmer', u'Summmy', u'UPSUMLY'] )


class WinnerAutoComplete(TestCase):
    def setUp(self):
        user = models.Userdata.objects.create(user_id=1, name="Sum", region_id=1, address="Sum", person="Marc")
        purchase = models.Purchase.objects.create(purchase_id=1, user=user, announce_id=1, goods_name="Nail")
        models.Winner.objects.create(winner_id=1, winner_name="Sallyone", purchase=purchase, winner_address="Kolombo",
                                     w_id=100)

        purchase = models.Purchase.objects.create(purchase_id=2, user=user, announce_id=2, goods_name="Desk")
        models.Winner.objects.create(winner_id=2, winner_name="Grek", purchase=purchase, winner_address="Kolombo",
                                     w_id=101)

        purchase = models.Purchase.objects.create(purchase_id=3, user=user, announce_id=3, goods_name="Cat")
        models.Winner.objects.create(winner_id=3, winner_name="Cat", purchase=purchase, winner_address="Kolombo",
                                     w_id=102)

        purchase = models.Purchase.objects.create(purchase_id=4, user=user, announce_id=4, goods_name="Sckuma")
        models.Winner.objects.create(winner_id=4, winner_name="Assally", purchase=purchase, winner_address="Kolombo",
                                     w_id=103)

        purchase = models.Purchase.objects.create(purchase_id=5, user=user, announce_id=5, goods_name="Glass")
        models.Winner.objects.create(winner_id=5, winner_name="Sally", purchase=purchase, winner_address="Kolombo",
                                     w_id=104)

        purchase = models.Purchase.objects.create(purchase_id=6, user=user, announce_id=6, goods_name="Board")
        models.Winner.objects.create(winner_id=6, winner_name="SallyTwo", purchase=purchase, winner_address="Kolombo",
                                     w_id=100)

        purchase = models.Purchase.objects.create(purchase_id=7, user=user, announce_id=7, goods_name="Apple")
        models.Winner.objects.create(winner_id=7, winner_name="blassyou", purchase=purchase, winner_address="Kolombo",
                                     w_id=101)

        purchase = models.Purchase.objects.create(purchase_id=8, user=user, announce_id=8, goods_name="Dorytos")
        models.Winner.objects.create(winner_id=8, winner_name="Wassally", purchase=purchase, winner_address="Kolombo",
                                     w_id=102)

        purchase = models.Purchase.objects.create(purchase_id=9, user=user, announce_id=9, goods_name="Caravans")
        models.Winner.objects.create(winner_id=9, winner_name="Kadjit", purchase=purchase, winner_address="Kolombo",
                                     w_id=103)

        purchase = models.Purchase.objects.create(purchase_id=10, user=user, announce_id=10, goods_name="Stone")
        models.Winner.objects.create(winner_id=10, winner_name="Poprally", purchase=purchase, winner_address="Kolombo",
                                     w_id=104)

    def test_WinnerAutoComplete(self):
        c = Client()
        response = c.get("/api/winnerAutocomplete/?name=Sally")

        self.assertEqual(json.loads(response.content),
                         [{u'label': u'Assally', u'value': u'Assally'},
                            {u'label': u'Sally', u'value': u'Sally'},
                            {u'label': u'Sallyone', u'value': u'Sallyone'},
                            {u'label': u'SallyTwo', u'value': u'SallyTwo'},
                            {u'label': u'Wassally', u'value': u'Wassally'}]
                         )
