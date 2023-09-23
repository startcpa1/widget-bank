from widget_bank.functions import extract_card_number


def test_extract_card_name():
    """Проверяет извлечение из строки номера"""
    test_account = 'MasterCard 1234567877771111'
    assert extract_card_number(test_account) == '1234567877771111'
