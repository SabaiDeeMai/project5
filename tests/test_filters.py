import pytest
from src.filters import filter_by_description, count_by_categories


def test_filter_by_description():
    transactions = [
        {"id": 1, "state": "EXECUTED", "description": "Оплата по счету"},
        {"id": 2, "state": "PENDING", "description": "Перевод на карту"},
        {"id": 3, "state": "EXECUTED", "description": "Перевод с карты на карту"},
        {"id": 4, "state": "CANCELED", "description": "Оплата за услуги"},
    ]

    result = filter_by_description(transactions, "оплата")
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 4

    result = filter_by_description(transactions, "перевод")
    assert len(result) == 2
    assert result[0]["id"] == 2
    assert result[1]["id"] == 3

    result = filter_by_description(transactions, "кредит")
    assert len(result) == 0

    result = filter_by_description(transactions, "ПЕРЕВОД")
    assert len(result) == 2
    assert result[0]["id"] == 2
    assert result[1]["id"] == 3


def test_count_by_categories():
    transactions = [
        {"id": 1, "state": "EXECUTED", "description": "Оплата по счету"},
        {"id": 2, "state": "PENDING", "description": "Перевод на карту"},
        {"id": 3, "state": "EXECUTED", "description": "Перевод с карты на карту"},
        {"id": 4, "state": "CANCELED", "description": "Оплата за услуги"},
    ]

    categories = ["оплата", "перевод"]

    result = count_by_categories(transactions, categories)

    assert result["оплата"] == 2
    assert result["перевод"] == 2

    result_empty = count_by_categories(transactions, [])
    assert result_empty == {}
