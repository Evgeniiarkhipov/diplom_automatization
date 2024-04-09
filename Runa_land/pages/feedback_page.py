from .locators import *
from .testing_data import *

LOGGER = logging.getLogger(__name__)
# Кнопка перехода на страницу обратной связи
class feedbackButton:
    def __init__(self, driver):
        self.feedback_button = driver.find_element(*feedback_button)
        LOGGER.info('Кнопка обратной связи найдена')
    def feedback_button_click(self):
        self.feedback_button.click()
        LOGGER.info('Кнопка нажата')

# Элементы заполнения и отправки заявки на странице обратной связи
class feedbackPage:
    def __init__(self, driver):
        self.customer_name = driver.find_element(*customer_name)
        self.customer_phone_or_email_input = driver.find_element(*customer_phone_or_email_input)
        self.input_text_input = driver.find_element(*input_text_input)
        self.send_feedback_button = driver.find_element(*send_feedback_button)
        LOGGER.info('Найдены все элементы заявки на обратную связь')

    def send_feedback(self, customer_name = '', customer_phone_or_email = '', input_text = ''):
        LOGGER.info('Начало заполнения заявки на обратную связь')
        self.customer_name.send_keys(customer_name)
        self.customer_phone_or_email_input.send_keys(customer_phone_or_email)
        self.input_text_input.send_keys(input_text)
        self.send_feedback_button.click()
        LOGGER.info('Конец заполнения заявки на обратную связь')