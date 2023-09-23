import json


def load_operations(filename):
    """Загружает операции из файла"""
    with open(filename) as file:
        operations = json.load(file)
    return operations


def format_date(date):
    """Получает дату операции в формате ДД.ММ.ГГГГ"""
    date_parts = date[0:10].split('-')
    formatted_date = '.'.join(reversed(date_parts))
    return formatted_date


def extract_card_number(from_account):
    """Извлекает номера карты или счета из поля отправителя"""
    card_number = ''
    if from_account:
        card_info = from_account.split(' ')
        for info in card_info:
            if info.isdigit():
                card_number = info
                break
    return card_number


def extract_card_name(from_account):
    """Извлекает название карты или счета"""
    card_name = ''
    if from_account:
        card_info = from_account.split(' ')
        for info in card_info:
            if info.isalpha():
                card_name = info
                break
    return card_name


def extract_account_name(to_account):
    """Извлекает информацию карты или счета получателя"""
    account_name = ''
    if to_account:
        account_info = to_account.split(' ')
        for info in account_info:
            if info.isalpha():
                account_name = info
                break
    return account_name


def mask_card_number(card_number):
    """Маскирует номер карты"""
    if card_number:
        masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        masked_card_number = 'N/A'
    return masked_card_number


def filter_executed_operations(operations):
    """Фильтрует операции EXECUTE"""
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    return executed_operations


def sort_operations_by_date(operations):
    """Сортирует операций по дате"""
    sorted_operations = sorted(operations, key=lambda x: x['date'], reverse=True)
    return sorted_operations


def display_recent_operations(filename):
    """Выводит последние 5 выполненных операций"""
    operations = load_operations(filename)
    executed_operations = filter_executed_operations(operations)
    sorted_operations = sort_operations_by_date(executed_operations)

    # Выводим последние 5 операций
    for operation in sorted_operations[:5]:
        date_operation = format_date(operation['date'])
        description = operation['description']
        from_account = operation.get('from')
        to_account = operation.get('to')
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']

        masked_from_account = '**' + from_account[-4:] if from_account else 'N/A'
        masked_to_account = '**' + to_account[-4:] if to_account else 'N/A'

        card_number = extract_card_number(from_account)
        card_name = extract_card_name(from_account)
        masked_card_number = mask_card_number(card_number)

        if card_name.startswith('Счет'):
            print(f"{date_operation} {description}\n{card_name} {masked_from_account}"
                  f" -> Счет {masked_to_account}\n{amount} {currency}\n")
        elif not card_name.startswith('Счет'):
            print(f"{date_operation} {description}\n{card_name} {masked_card_number}"
                  f" -> Счет {masked_to_account}\n{amount} {currency}\n")
