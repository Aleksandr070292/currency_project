from django.test import TestCase
from .models import ExchangeRateRequest
from django.urls import reverse
import time


class ExchangeRateTests(TestCase):
    def test_get_current_usd(self):
        response = self.client.get(reverse('get_current_usd'))
        self.assertEqual(response.status_code, 200 or 429)

    def test_request_interval(self):
        # Делаем два запроса подряд, второй должен вернуть ошибку 429
        response1 = self.client.get(reverse('get_current_usd'))
        time.sleep(1)
        response2 = self.client.get(reverse('get_current_usd'))
        self.assertEqual(response2.status_code, 429)
