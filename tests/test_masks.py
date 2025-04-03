import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [
    ("1234567812345678", "1234 56** **** 5678"),
    ("9876543210987654", "9876 54** **** 7654")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account_number, expected", [
    ("1234567890123456", "** 3456"),
    ("987654321098", "** 1098")
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
