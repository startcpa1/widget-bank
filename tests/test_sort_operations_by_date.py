from widget_bank.functions import sort_operations_by_date


def test_sort_operations():
    """Проверяет сортировку по дате"""
    operations = [
        {'date': '2023-06-20', 'amount': 100},
        {'date': '2023-06-18', 'amount': 200},
        {'date': '2023-06-19', 'amount': 300}
    ]

    expected_result = [
        {'date': '2023-06-20', 'amount': 100},
        {'date': '2023-06-19', 'amount': 300},
        {'date': '2023-06-18', 'amount': 200}
    ]

    assert sort_operations_by_date(operations) == expected_result
