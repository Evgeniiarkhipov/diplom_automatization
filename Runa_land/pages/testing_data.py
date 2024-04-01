# Подключение логирования
import logging
logger = logging.getLogger(__name__)
handler = logging.FileHandler(f'logs/runa_land.log', mode='w', encoding='utf-8')
formatter = logging.Formatter(f'{__name__} %(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
def data_application(data):
    for k, v, in enumerate(data):
        data[k] = v['property_type'], v['direction'], v['start_price'], v['end_price'], v['customer_name'], v['customer_phone'], v['customer_email']
    logger.info('Тестовые данные заявки на тур')
    return data
def data_feedback(data):
    for k, v in enumerate(data):
        data[k] = v['customer_name'], v['customer_phone_or_email'], v['input_text'], v['expected_url']
    logger.info('Тестовые данные обратной связи')
    return data

# Тестовые данные для формы заполнения заявки на тур на главной странице
test_cases_application = [
# Позитивный сценарий
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
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экстримальный',
     'direction': 'Беломорский район',
     'start_price': '4000',
     'end_price': '5000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
# Негативный сценарий
    {
     'property_type': 'Экстримальный',
     'direction': 'Калевальский район',
     'start_price': '7000',
     'end_price': '30000',
     'customer_name': '',
     'customer_phone': '9110000009',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Семейный',
     'direction': 'Лоухи',
     'start_price': '3000',
     'end_price': '20000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экскурсионный',
     'direction': 'Сегежский',
     'start_price': '',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '+79110000000',
     'customer_email': 'test@test.ru'
    }
]

# Тестовые данные для формы заполнения заявки на странице обратной связи
test_cases_feedback = [
# Позитивный сценарий
    {
        'customer_name': 'Тестовое_имя',
        'customer_phone_or_email': 'test@test.ru',
        'input_text': 'Тестовая строка',
        'expected_url': 'thank'
    },
# Негативный сценарий
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