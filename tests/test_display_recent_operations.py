from widget_bank.functions import display_recent_operations

filename = 'demo.json'


def test_display_recent_operations():
    """Проверяет вывод операций ранее отсортированных по EXECUTE"""
    assert display_recent_operations(filename) == None
