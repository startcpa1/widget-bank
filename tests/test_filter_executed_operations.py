from widget_bank.functions import filter_executed_operations


def test_filter_executed_operations():
    """Проверяет фильтрацию по операциям со статусом EXECUTED"""
    operations = [
        {'id': 1, 'state': 'CANCELED'},
        {'id': 2, 'state': 'EXECUTED'},
        {'id': 3, 'state': 'PENDING'},
        {'id': 4, 'state': 'EXECUTED'},
    ]

    result = filter_executed_operations(operations)
    assert len(result) == 2
    assert result[0]['id'] == 2
    assert result[1]['id'] == 4
