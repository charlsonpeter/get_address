from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# Create your tests here.


class GetAddressTest(APITestCase):
    def not_in_db(self):
        resp = self.client.get("/location/get_address/9.999/10.545/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def in_db(self):
        resp = self.client.get("/location/get_address/9.999/10.545/")
        resp = self.client.get("/location/get_address/9.999/10.545/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
