import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)

# Входные данные
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
]


@pytest.mark.parametrize(
    "currency, expected_count",
    [("USD", 2), ("RUB", 1), ("EUR", 0)],  # Проверка отсутствующих транзакций
)
def test_filter_by_currency(currency, expected_count):
    result = list(filter_by_currency(transactions, currency))
    assert len(result) == expected_count


def test_transaction_descriptions():
    descriptions = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    print(list(transaction_descriptions(transactions)))
    assert descriptions == expected


def test_card_number_generator():
    gen = card_number_generator("0000 0000 0000 0001", "0000 0000 0000 0010")
    generated = list(gen)
    assert len(generated) == 10
    assert generated[0] == "0000 0000 0000 0001"
    assert generated[-1] == "0000 0000 0000 0010"
