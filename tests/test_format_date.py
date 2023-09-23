from widget_bank.functions import format_date


def test_format_date():
    """Проверяет форматирование даты"""
    date_ = '2019-08-26'
    assert format_date(date_) == '26.08.2019'