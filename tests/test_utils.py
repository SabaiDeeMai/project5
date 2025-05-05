from unittest.mock import mock_open, patch

from src.utils import load_transactions


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_load_valid_transactions(mock_file):
    result = load_transactions("data/operations.json")
    assert result == [{"amount": 100, "currency": "USD"}]


@patch("builtins.open", new_callable=mock_open, read_data='{}')
def test_load_invalid_format(mock_file):
    result = load_transactions("data/operations.json")
    assert result == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file):
    result = load_transactions("data/operations.json")
    assert result == []
