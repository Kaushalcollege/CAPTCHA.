import os
from django.conf import settings
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Different.settings')

class PredictBotViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_predict_bot(self):
        # Sample data
        data = {
            'round_trip_time': 200,
            'country': 'US',
            'browser': 'Chrome 90',
            'os': 'Windows 10',
            'login_timestamp': 1627814400,
            'login_successful': 1
        }

        response = self.client.post('/predict/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Optionally, check if the response contains expected keys
        self.assertIn('is_bot', response.data)
