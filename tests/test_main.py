import pytest
from collections import Counter
from src.main import (
    filter_by_status,
    sort_transactions,
    filter_rubles,
    count_transactions_by_category
)

sample_transactions = [
    {
        "state": "EXECUTED",
        "date": "2023-09-01T10:00:00.000",
        "description": "Перевод организации",
        "from": "Счет **1234",
        "to": "Счет **5678",
        "operationAmount": {
            "amount": 5000,
            "currency": {"code": "RUB", "name": "руб."}
        }
    },
    {
        "state": "CANCELED",
        "date": "2022-01-10T09:15:00.000",
        "description": "Перевод физическому лицу",
        "from": "Счет **2345",
        "to": "Счет **6789",
        "operationAmount": {
            "amount": 7000,
            "currency": {"code": "USD", "name": "USD"}
        }
    },
    {
        "state": "EXECUTED",
        "date": "2021-05-03T12:30:00.000",
        "description": "Открытие вклада",
        "from": "",
        "to": "Счет **0001",
        "operationAmount": {
            "amount": 10000,
            "currency": {"code": "RUB", "name": "руб."}
        }
    },
]


def test_filter_by_status():
    result = filter_by_status(sample_transactions, "EXECUTED")
    assert len(result) == 2
    assert all(txn["state"] == "EXECUTED" for txn in result)


def test_sort_transactions_ascending():
    result = sort_transactions(sample_transactions, ascending=True)
    dates = [txn["date"] for txn in result]
    assert dates == sorted(dates)


def test_sort_transactions_descending():
    result = sort_transactions(sample_transactions, ascending=False)
    dates = [txn["date"] for txn in result]
    assert dates == sorted(dates, reverse=True)


def test_filter_rubles():
    result = filter_rubles(sample_transactions)
    assert all(txn["__currency_code"] == "RUB" for txn in result)
    assert len(result) == 2


def test_count_transactions_by_category():
    result = count_transactions_by_category(sample_transactions)
    expected = {
        "Перевод организации": 1,
        "Перевод физическому лицу": 1,
        "Открытие вклада": 1
    }
    assert result == expected
