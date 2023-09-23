from widget_bank.functions import extract_card_name


def test_extract_card_name():
    """Проверяет извлечение названия карты"""
    test_account = 'MasterCard 1234567877771111'
    assert extract_card_name(test_account) == 'MasterCard'
