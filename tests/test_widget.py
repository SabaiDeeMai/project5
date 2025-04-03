import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("input_str, expected", [
    ("Visa 1234567812345678", "Visa 1234 56** **** 5678"),
    ("Счет 1234567890", "Счет ** 7890")
])
def test_mask_account_card(input_str, expected):
    assert mask_account_card(input_str) == expected


@pytest.mark.parametrize("date_str, expected", [
    ("2024-03-31T12:00:00.000000", "31.03.2024"),
    ("2023-01-15T08:45:30.123456", "15.01.2023")
])
def test_get_date(date_str, expected):
    assert get_date(date_str) == expected
