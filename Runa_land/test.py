import time
from pages.testing_data import *
from pages.application_page import applicationPage
from pages.feedback_page import feedbackPage, feedbackButton
import pytest
from selenium import webdriver
from config import *

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get(base_url)
    driver.implicitly_wait(5)

    yield driver
    driver.quit()

@pytest.mark.parametrize('property_type, direction, start_price, end_price, customer_name, customer_phone, customer_email', data_application(test_cases_application))

def test_case_full_application(browser, property_type, direction, start_price, end_price, customer_name, customer_phone, customer_email):
    application_page = applicationPage(browser)
    application_page.application(browser, property_type, direction, start_price, end_price, customer_name, customer_phone, customer_email)

@pytest.mark.parametrize('customer_name, customer_phone_or_email, input_text, expected_url', data_feedback(test_cases_feedback))

def test_case_feedback(browser, customer_name, customer_phone_or_email, input_text, expected_url):
    feedback_button = feedbackButton(browser)
    feedback_button.feedback_button_click()
    feedback_page = feedbackPage(browser)
    feedback_page.send_feedback(customer_name, customer_phone_or_email, input_text)
    assert browser.current_url == base_url + expected_url