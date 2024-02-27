from .locators import *

class feedbackButton:
    # Атрибуты
    def __init__(self, driver):
        self.feedback_button = driver.find_element(*feedback_button)
    # Методы
    def feedback_button_click(self):
        self.feedback_button.click()

class feedbackPage:
    # Атрибуты
    def __init__(self, driver):
        self.customer_name = driver.find_element(*customer_name)
        self.customer_phone_or_email_input = driver.find_element(*customer_phone_or_email_input)
        self.input_text_input = driver.find_element(*input_text_input)
        self.send_feedback_button = driver.find_element(*send_feedback_button)

    # Методы
    def send_feedback(self, customer_name = '', customer_phone_or_email = '', input_text = ''):
        self.customer_name.send_keys(customer_name)
        self.customer_phone_or_email_input.send_keys(customer_phone_or_email)
        self.input_text_input.send_keys(input_text)
        self.send_feedback_button.click()