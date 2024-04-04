from selenium.webdriver.common.by import By

'''
Локаторы для полей ввода на главной странице (application_page)
'''
# Поля ввода заявки на тур
rest = (By.XPATH, '//*[@id="form1"]/div[1]/div[2]/div/span[2]')
rest_focus = (By.XPATH, '//*[@id="form1"]/div[1]/div[2]/div/div/ul/li[2]')

css_locator_rest = '#form1 > div.tpl-field.type-select.field-required.type.select-data1 > div.field-value > div > span.selected'
property_values_rest = (By.CSS_SELECTOR, css_locator_rest)

region = (By.XPATH, '//*[@id="form1"]/div[2]/div[2]/div/span[2]')
region_focus = (By.XPATH, '//*[@id="form1"]/div[2]/div[2]/div/div/ul/li[2]')

css_locator_region = '#form1 > div.tpl-field.type-select.field-required.direction.select-data2 > div.field-value > div > span.selected'
property_values_region = (By.CSS_SELECTOR, css_locator_region)

start_price_input = (By.XPATH, '//*[@id="form1"]/div[3]/div[2]/label[1]/input')
end_price_input = (By.XPATH, '//*[@id="form1"]/div[3]/div[2]/label[2]/input')

start_date_input = (By.XPATH, '//*[@id="tcalico_0"]')
date_s = (By.XPATH, '//*[@id="tcal"]/table[2]/tbody/tr[4]/td[4]')

end_date_input = (By.XPATH, '//*[@id="tcalico_1"]')
date_e = (By.XPATH, '//*[@id="tcal"]/table[2]/tbody/tr[4]/td[3]')

customer_name_input = (By.XPATH, '//*[@id="form1"]/div[5]/div[2]/input')
customer_phone_input = (By.XPATH, '//*[@id="form1"]/div[6]/div[2]/input')
customer_email_input = (By.XPATH, '//*[@id="form1"]/div[7]/div[2]/input')

# Кнопка отправки заявки на тур
application_button = (By.XPATH, '//*[@id="form1"]/div[8]/button')

'''
Локаторы ошибочных полей ввода
'''
list_locators = ['selected error',
                 'price-label error',
                 'field-value error']

'''
Локаторы на странице обратной связи (feedback_page)
'''
# Поля ввода
feedback_button = (By.XPATH, '/html/body/div[2]/header/div/div[2]/div[3]/a')
customer_name = (By.XPATH, '//*[@id="d[0]"]')
customer_phone_or_email_input = (By.XPATH, '//*[@id="d[1]"]')
input_text_input = (By.XPATH, '//*[@id="d[2]"]')

# Кнопка отправки заявки обратной связи
send_feedback_button = (By.XPATH, '//*[@id="form2"]/button')