from .locators import *

class applicationPage:
    # Атрибуты
    def __init__(self, driver):
        self.rest = driver.find_element(*rest)
        self.rest_focus = driver.find_element(*rest_focus)
        self.property_values_rest = driver.find_element(*property_values_rest)

        self.region = driver.find_element(*region)
        self.region_focus = driver.find_element(*region_focus)
        self.property_values_region = driver.find_element(*property_values_region)

        self.start_price_input = driver.find_element(*start_price_input)
        self.end_price_input = driver.find_element(*end_price_input)

        self.start_date_input = driver.find_element(*start_date_input)
        # self.date_s = driver.find_element(*date_s)

        self.end_date_input = driver.find_element(*end_date_input)
        # self.date_e = driver.find_element(*date_e)

        self.customer_name_input = driver.find_element(*customer_name_input)
        self.customer_phone_input = driver.find_element(*customer_phone_input)
        self.customer_email_input = driver.find_element(*customer_email_input)

        self.button = driver.find_element(*application_button)

    # Методы
    def application(self, driver, property_type = '', direction = '', start_price = '', end_price = '', customer_name = '', customer_phone = '', customer_email = ''):
        self.rest.click()
        self.rest_focus.click()
        driver.execute_script(f"ele=arguments[0]; ele.innerHTML = '{property_type}';", property_values_rest);

        self.region.click()
        self.region_focus.click()
        driver.execute_script(f"ele=arguments[0]; ele.innerHTML = '{direction}';", property_values_region);

        self.start_price_input.click()
        self.start_price_input.send_keys(start_price)

        self.end_price_input.click()
        self.end_price_input.send_keys(end_price)

        self.start_date_input.click()
        self.date_s = driver.find_element(*date_s)
        self.date_s.click()

        self.end_date_input.click()
        self.date_e = driver.find_element(*date_e)
        self.date_e.click()

        self.customer_name_input.send_keys(customer_name)
        self.customer_phone_input.send_keys(customer_phone)
        self.customer_email_input.send_keys(customer_email)

        self.button.click()