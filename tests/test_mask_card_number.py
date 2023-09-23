from widget_bank.functions import mask_card_number


def test_mask_card_number():
    """Проверяет маскировку номера карты"""
    card_number = '1234567877779999'
    card_no_valid = ''
    assert mask_card_number(card_number) == '1234 56** **** 9999'
    assert mask_card_number(card_no_valid) == 'N/A'
