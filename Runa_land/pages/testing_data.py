def data_application(data):
    for k, v, in enumerate(data):
        data[k] = v['property_type'], v['direction'], v['start_price'], v['end_price'], v['customer_name'], v['customer_phone'], v['customer_email']
    return data
def data_feedback(data):
    for k, v in enumerate(data):
        data[k] = v['customer_name'], v['customer_phone_or_email'], v['input_text'], v['expected_url']
    return data

test_cases_application = [
    {
     'property_type': 'Семейный',
     'direction': 'Петрозаводск',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экскурсионный',
     'direction': 'Кондопожский район',
     'start_price': '20000',
     'end_price': '60000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'invalidmailtest.ru'
    },
    {
     'property_type': 'Экстримальный',
     'direction': 'Беломорский район',
     'start_price': '4000',
     'end_price': '5000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '911000000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экстримальный',
     'direction': 'Калевальский район',
     'start_price': '7000',
     'end_price': '30000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000009',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Семейный',
     'direction': 'Лоухи',
     'start_price': '3000',
     'end_price': '20000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '+79110000000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экскурсионный',
     'direction': 'Сегежский',
     'start_price': '5000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '+79110000000',
     'customer_email': 'test@test.ru'
    }
]
test_cases_feedback = [
    {
        'customer_name': 'Тестовое_имя',
        'customer_phone_or_email': 'test@test.ru',
        'input_text': 'Тестовая строка',
        'expected_url': 'thank'
    },
    {
        'customer_name': '',
        'customer_phone_or_email': 'invalidemail.com',
        'input_text': 'Тестовая строка_2',
        'expected_url': 'mail'
    },
    {
        'customer_name': 'Тестовое_имя',
        'customer_phone_or_email': 'invalidemail.com',
        'input_text': 'Тестовая строка_2',
        'expected_url': 'mail'
    },
    {
        'customer_name': 'Тестовое_имя',
        'customer_phone_or_email': 'invalidemail.com',
        'input_text': '',
        'expected_url': 'mail'
    }
]