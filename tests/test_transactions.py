import pytest
from unittest.mock import patch, mock_open, MagicMock
from src import transactions
import pandas as pd


def test_get_read_csv_transact():
    csv_content = (
        "id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "1;EXECUTED;2024-01-01;1000;RUB;643;Alice;Bob;Test transfer\n"
    )

    mocked_open = mock_open(read_data=csv_content)

    with patch("builtins.open", mocked_open):
        result = transactions.get_read_csv_transact("fake_path.csv")

    expected = [{
        "id": "1",
        "state": "EXECUTED",
        "date": "2024-01-01",
        "amount": "1000",
        "currency_name": "RUB",
        "currency_code": "643",
        "from": "Alice",
        "to": "Bob",
        "description": "Test transfer"
    }]

    assert result == expected


@patch("pandas.read_excel")
def test_get_read_excel_transact(mock_read_excel):
    mock_df = pd.DataFrame([{
        "id": "2", "state": "EXECUTED", "date": "2024-01-02", "amount": "2000",
        "currency_name": "USD", "currency_code": "840", "from": "Charlie",
        "to": "Dave", "description": "Salary"
    }])
    mock_read_excel.return_value = mock_df

    result = transactions.get_read_excel_transact("fake_path.xlsx")

    expected = [{
        "id": "2",
        "state": "EXECUTED",
        "date": "2024-01-02",
        "amount": "2000",
        "currency_name": "USD",
        "currency_code": "840",
        "from": "Charlie",
        "to": "Dave",
        "description": "Salary"
    }]

    assert result == expected
    mock_read_excel.assert_called_once_with("fake_path.xlsx", dtype=str, engine="openpyxl")


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_get_read_excel_transact_file_not_found(mock_read_excel):
    result = transactions.get_read_excel_transact("nonexistent.xlsx")
    assert result == []

