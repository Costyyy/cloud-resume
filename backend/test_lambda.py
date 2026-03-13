import json
from unittest.mock import MagicMock, patch
import lambda_function

@patch("lambda_function.table")
def test_returns_count(mock_table):
    mock_table.update_item.return_value = {
        "Attributes": {"visitor_count": 42}
    }

    result = lambda_function.lambda_handler({}, {})
    body = json.loads(result["body"])

    assert result["statusCode"] == 200
    assert body["count"] == 42

@patch("lambda_function.table")
def test_increments_count(mock_table):
    mock_table.update_item.return_value = {
        "Attributes": {"visitor_count": 1}
    }

    lambda_function.lambda_handler({}, {})

    mock_table.update_item.assert_called_once()
    call_args = mock_table.update_item.call_args[1]
    assert call_args["ExpressionAttributeValues"][":inc"] == 1
