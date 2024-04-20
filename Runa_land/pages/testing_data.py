# Подключение логирования
import logging
import datetime
date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
logger = logging.getLogger()
handler = logging.FileHandler(f'logs/runa_land{date}.log', mode='w', encoding='utf-8')
formatter = logging.Formatter(f'%(module)s %(asctime)s %(levelname)s %(message)s')
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
# Семейный отдых
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
     'property_type': 'Семейный',
     'direction': 'Кондопожский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Семейный',
     'direction': 'Беломорский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Семейный',
     'direction': 'Сортавальский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Семейный',
     'direction': 'Кемьский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Семейный',
     'direction': 'Калевальский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Семейный',
     'direction': 'Лоухи',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Семейный',
     'direction': 'Сегежский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Семейный',
     'direction': 'Медвежьегорский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Семейный',
     'direction': 'Суоярви',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Семейный',
     'direction': 'Не имеет значения',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
# Экскурсионный отдых
    {
     'property_type': 'Экскурсионный',
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
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экскурсионный',
     'direction': 'Беломорский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экскурсионный',
     'direction': 'Сортавальский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экскурсионный',
     'direction': 'Кемьский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экскурсионный',
     'direction': 'Калевальский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экскурсионный',
     'direction': 'Лоухи',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экскурсионный',
     'direction': 'Сегежский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экскурсионный',
     'direction': 'Медвежьегорский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экскурсионный',
     'direction': 'Суоярви',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экскурсионный',
     'direction': 'Не имеет значения',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
# Экстремальный отдых
    {
     'property_type': 'Экстремальный',
     'direction': 'Петрозаводск',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экстремальный',
     'direction': 'Кондопожский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экстремальный',
     'direction': 'Беломорский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экстремальный',
     'direction': 'Сортавальский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экстремальный',
     'direction': 'Кемьский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экстремальный',
     'direction': 'Калевальский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экстремальный',
     'direction': 'Лоухи',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экстремальный',
     'direction': 'Сегежский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экстремальный',
     'direction': 'Медвежьегорский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экстремальный',
     'direction': 'Суоярви',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Экстремальный',
     'direction': 'Не имеет значения',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
# Активный отдых
    {
     'property_type': 'Активный',
     'direction': 'Петрозаводск',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Активный',
     'direction': 'Кондопожский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Активный',
     'direction': 'Беломорский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Активный',
     'direction': 'Сортавальский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Активный',
     'direction': 'Кемьский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Активный',
     'direction': 'Калевальский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Активный',
     'direction': 'Лоухи',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Активный',
     'direction': 'Сегежский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Активный',
     'direction': 'Медвежьегорский район',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Активный',
     'direction': 'Суоярви',
     'start_price': '10000',
     'end_price': '50000',
     'customer_name': 'Тестовое_имя',
     'customer_phone': '9110000000',
     'customer_email': 'test@test.ru'
    },
    {
     'property_type': 'Активный',
     'direction': 'Не имеет значения',
     'start_price': '10000',
     'end_price': '50000',
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