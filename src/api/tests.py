import json

from rest_framework.response import Response
from rest_framework.test import (
    APIClient,
    APITestCase,
)


class SimpleTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def create_category(self):
        return self.client.post("/api/v1/categories/", {"name": "category1"})

    def create_item(self):
        return self.client.post(
            "/api/v1/items/",
            {"categories": ["category1"], "name": "item1", "price": 100},
        )

    def test_empty_items_list(self):
        res: Response = self.client.get("/api/v1/items/")
        self.assertEquals(res.status_code, 200)
        res_json = json.loads(res.content)
        self.assertEquals(
            res_json, {"count": 0, "next": None, "previous": None, "results": []}
        )

    def test_create_category(self):
        res: Response = self.create_category()
        self.assertEquals(res.status_code, 201)
        res_json = json.loads(res.content)
        self.assertEquals(res_json, {"id": 1, "name": "category1"})

    def test_delete_category(self):
        res = self.create_category()
        category_id = json.loads(res.content)["id"]
        res: Response = self.client.delete(f"/api/v1/categories/{category_id}/")
        self.assertEquals(res.status_code, 204)

    def test_create_item(self):
        self.create_category()
        res: Response = self.create_item()
        self.assertEquals(res.status_code, 201)
        res_json = json.loads(res.content)
        item_id = res_json["id"]
        self.assertEquals(
            res_json,
            {
                "id": item_id,
                "categories": ["category1"],
                "name": "item1",
                "price": 100.0,
                "published": False,
            },
        )

    def test_delete_item(self):
        self.create_category()
        res = self.create_item()
        item_id = json.loads(res.content)["id"]
        res: Response = self.client.delete(f"/api/v1/items/{item_id}/")
        self.assertEquals(res.status_code, 204)

    def test_delete_category_with_items(self):
        res = self.create_category()
        self.create_item()
        category_id = json.loads(res.content)["id"]
        res: Response = self.client.delete(f"/api/v1/categories/{category_id}/")
        self.assertEquals(res.status_code, 400)
