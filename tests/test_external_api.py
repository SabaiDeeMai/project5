from unittest.mock import MagicMock, patch

from src.external_api import convert_to_rub


@patch("src.external_api.requests.request")
def test_convert_usd_success(mock_request):
    # Настраиваем фейковый ответ API
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 13999.5}
    mock_request.return_value = mock_response

    transaction = {"amount": 150.0, "currency": "USD"}
    result = convert_to_rub(transaction)

    assert result == 13999.5


@patch("src.external_api.requests.request", side_effect=Exception("API error"))
def test_convert_api_error_returns_zero(mock_get):
    transaction = {"amount": 200.0, "currency": "EUR"}
    result = convert_to_rub(transaction)

    assert result == 0.0
