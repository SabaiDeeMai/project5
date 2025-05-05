import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

API_URL = "https://api.apilayer.com/exchangerates_data/convert"


def convert_to_rub(transaction: dict) -> float:
    """
    Преобразует сумму транзакции в рубли, используя Exchange Rates Data API.
    """
    amount = transaction.get("amount")
    currency = transaction.get("currency")

    if not amount or not currency:
        return 0.0

    if currency == "RUB":
        return float(amount)

    params = {
        "to": "rub",
        "from": currency,
        "amount": amount
    }

    headers = {
        "apikey": API_KEY
    }

    try:
        response = requests.request("GET", API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return float(data["result"])
    except (requests.RequestException, KeyError, ValueError, TypeError, Exception):
        return 0.0
