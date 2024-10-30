from django.http import JsonResponse
from django.utils import timezone
from .models import ExchangeRateRequest
import requests


def get_current_usd(request):
    # Проверка времени последнего запроса
    last_request = ExchangeRateRequest.objects.last()
    if last_request and (timezone.now() - last_request.timestamp).seconds < 10:
        return JsonResponse({"error": "Too many requests. Please wait 10 seconds."}, status=429)

    # Вызов внешнего API
    try:
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        response.raise_for_status()
        data = response.json()
        usd_to_rub = data["rates"]["RUB"]

        # Сохранение нового запроса в базу
        ExchangeRateRequest.objects.create(rate=usd_to_rub)

        # Получение последних 10 запросов
        last_10_requests = ExchangeRateRequest.objects.order_by('-timestamp')[:10]

        return JsonResponse({
            "current_rate": usd_to_rub,
            "last_10_requests": [{"rate": req.rate, "timestamp": req.timestamp} for req in last_10_requests]
        })

    except requests.RequestException:
        return JsonResponse({"error": "Failed to fetch the exchange rate."}, status=500)
