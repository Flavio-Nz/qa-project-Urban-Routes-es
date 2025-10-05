import time
import data
import helpers
from helpers import retrieve_phone_code
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    taxi_button = (By.CSS_SELECTOR, 'button.round')
    comfort_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]')
    input_phone = (By.CLASS_NAME, 'np-text')
    input_phone_modal = (By.XPATH, '//*[@id="phone"]')
    submit_button_phone_modal = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    phone_code_input = (By.CSS_SELECTOR, '[placeholder="xxxx"]')
    submit_code_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    phone_number = (By.CLASS_NAME, 'np-text')
    payment_method_input = (By.CLASS_NAME, 'pp-button.filled')
    credit_card_input = (By.CLASS_NAME, 'pp-row.disabled')
    card_number_input = (By.XPATH, '//*[@id="number"]')
    card_code_input = (By.CSS_SELECTOR, 'input#code.card-input')
    remove_cvv_focus = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[2]')
    add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_card_modal_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    card_input_value = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]')
    driver_message_input = (By.CSS_SELECTOR, 'input#comment.input')
    error_message = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[3]/div[2]')
    blanked_switch = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div')
    ice_cream_add_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    ice_cream_quantity = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    reserve_button = (By.CLASS_NAME, 'smart-button')
    taxi_modal = (By.CLASS_NAME, 'order-body')
    order_number = (By.CLASS_NAME, 'order-number')
    taxi_modal_text = (By.CLASS_NAME, 'order-header-title')


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    #Definición del paso para establecer la ruta
    def set_route(self, desde, hasta):
        self.set_from(desde)
        self.set_to(hasta)
        self.get_from()
        self.get_to()
        time.sleep(.5)

    def click_taxi_button(self):
        self.driver.find_element(*self.taxi_button).click()
        time.sleep(.5)

    def click_comfort_button(self):
        self.driver.find_element(*self.comfort_button).click()
        time.sleep(.5)

    def check_comfort_button_selected(self):
        return self.driver.find_element(*self.comfort_button).get_attribute('class')

    #Paso para seleccionar la tarifa comfort
    def set_comfort_tariff(self):
        self.click_taxi_button()
        self.click_comfort_button()

    #Teléfono
    def click_input_phone(self):
        self.driver.find_element(*self.input_phone).click()
        time.sleep(.5)

    def set_input_phone_modal(self):
        self.driver.find_element(*self.input_phone_modal).send_keys(data.phone_number)
        time.sleep(.5)

    def click_submit_button_phone_modal(self):
        self.driver.find_element(*self.submit_button_phone_modal).click()
        time.sleep(.5)

    def set_phone_code_input(self):
        code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.phone_code_input).send_keys(code)
        time.sleep(.5)

    def click_submit_code_button(self):
        self.driver.find_element(*self.submit_code_button).click()
        time.sleep(.5)

    #Paso para introducir el número de teléfono
    def set_phone_number (self):
        self.click_input_phone()
        self.set_input_phone_modal()
        self.click_submit_button_phone_modal()
        self.set_phone_code_input()
        self.click_submit_code_button()
        self.get_phone_number()

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number).text

    #Metodo de pago
    def click_payment_method_input(self):
        self.driver.find_element(*self.payment_method_input).click()
        time.sleep(.5)

    def click_credit_card_input(self):
        self.driver.find_element(*self.credit_card_input).click()
        time.sleep(.5)

    def set_card_number(self):
        self.driver.find_element(*self.card_number_input).send_keys(data.card_number)
        time.sleep(.5)

    def set_card_code(self):
        self.driver.find_element(*self.card_code_input).send_keys(data.card_code)
        time.sleep(.5)

    def click_remove_focus(self):
        self.driver.find_element(*self.remove_cvv_focus).click()
        time.sleep(.5)

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()
        time.sleep(.5)

    def close_payment_modal(self):
        self.driver.find_element(*self.close_card_modal_button).click()
        time.sleep(.5)

    #Pasos para agregar tarjeta de crédito
    def add_credit_card(self):
        self.driver.implicitly_wait(3)
        self.click_payment_method_input()
        self.click_credit_card_input()
        self.set_card_number()
        self.set_card_code()
        self.click_remove_focus()
        self.click_add_card_button()
        self.close_payment_modal()
        return self.driver.find_element(*self.card_input_value).text

    def check_payment_method(self):
        return self.driver.find_element(*self.card_input_value).text

    def set_driver_message(self):
        self.driver.find_element(*self.driver_message_input).send_keys(data.message_for_driver)
        time.sleep(.5)

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def validate_error_message(self):
        self.set_driver_message()
        self.get_error_message()

    def toggle_blanket_switch(self):
        self.driver.find_element(*self.blanked_switch).click()
        time.sleep(1)

    def validate_blanket_switch(self):
        return self.driver.find_element(*self.blanked_switch).is_selected()

    def add_ice_cream(self):
        self.driver.find_element(*self.ice_cream_add_button).click()
        time.sleep(.5)
        self.driver.find_element(*self.ice_cream_add_button).click()
        time.sleep(1)

    def get_ice_cream_quantity(self):
        return self.driver.find_element(*self.ice_cream_quantity).text

    def validate_ice_cream(self):
        self.add_ice_cream()
        self.get_ice_cream_quantity()

    def click_reserve_button(self):
        self.driver.find_element(*self.reserve_button).click()

    def validate_modal_is_visible(self):
        return self.driver.find_element(*self.taxi_modal).is_displayed()

    #esperar a que se muestren datos del taxi
    def wait_for_driver_data(self):
        self.wait.until(expected_conditions.visibility_of_element_located(*self.order_number))

    def validate_taxi_modal_text(self):
        return self.driver.find_element(*self.taxi_modal_text).text

    def validate_order_data(self):
        return self.driver.find_element(*self.order_number).is_displayed()


