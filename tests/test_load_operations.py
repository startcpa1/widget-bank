import os
from widget_bank.functions import load_operations

filename = 'test.json'


def test_load_operations():
    """Проверяет загрузку из файла"""
    dir_name = os.path.dirname(__file__)
    file_path = os.path.join(dir_name, filename)
    assert load_operations(file_path) == [1, 2, 3, 4]
