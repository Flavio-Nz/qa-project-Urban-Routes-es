import time
import data
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
    ice_cream_quantity = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]')
    reserve_button = (By.CLASS_NAME, 'smart-button')
    taxi_modal = (By.CLASS_NAME, 'order-body')
    order_number = (By.CLASS_NAME, 'order-number')
    taxi_modal_text = (By.CLASS_NAME, 'order-header-title')


    def __init__(self, driver):
        self.driver = driver

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

    def click_taxi_button(self):
        self.driver.find_element(*self.taxi_button).click()

    def click_comfort_button(self):
        self.driver.find_element(*self.comfort_button).click()

    def check_comfort_button_selected(self):
        return self.driver.find_element(*self.comfort_button).get_attribute('class')

    #Paso para seleccionar la tarifa comfort
    def set_comfort_tariff(self):
        self.click_taxi_button()
        self.click_comfort_button()

    #Teléfono
    def click_input_phone(self):
        self.driver.find_element(*self.input_phone).click()

    def set_input_phone_modal(self):
        self.driver.find_element(*self.input_phone_modal).send_keys(data.phone_number)

    def click_submit_button_phone_modal(self):
        self.driver.find_element(*self.submit_button_phone_modal).click()

    ###################

    # no modificar
    def retrieve_phone_code(driver) -> str:
        """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
        Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
        El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

        import json
        import time
        from selenium.common import WebDriverException
        code = None
        for i in range(10):
            try:
                logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                        and 'api/v1/number?number' in log.get("message")]
                for log in reversed(logs):
                    message_data = json.loads(log)["message"]
                    body = driver.execute_cdp_cmd('Network.getResponseBody',
                                                  {'requestId': message_data["params"]["requestId"]})
                    code = ''.join([x for x in body['body'] if x.isdigit()])
            except WebDriverException:
                time.sleep(1)
                continue
            if not code:
                raise Exception("No se encontró el código de confirmación del teléfono.\n"
                                "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
            return code

    ###################

    def set_phone_code_input(self):
        self.driver.find_element(*self.phone_code_input).send_keys(*self.retrieve_phone_code())

    def click_submit_code_button(self):
        self.driver.find_element(*self.submit_code_button).click()

    #Paso para introducir el número de teléfono
    def set_phone_number (self):
        self.click_input_phone()
        self.set_input_phone_modal()
        self.click_submit_button_phone_modal()
        self.retrieve_phone_code()
        self.set_phone_code_input()
        self.click_submit_code_button()

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number).get_property('value')

    #Metodo de pago
    def click_payment_method_input(self):
        self.driver.find_element(*self.payment_method_input).click()

    def click_credit_card_input(self):
        self.driver.find_element(*self.credit_card_input).click()

    def set_card_number(self):
        self.driver.find_element(*self.card_number_input).send_keys(data.card_number)

    def set_card_code(self):
        self.driver.find_element(*self.card_code_input).send_keys(data.card_code)

    def click_remove_focus(self):
        self.driver.find_element(*self.remove_cvv_focus).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.add_card_button).click()

    def close_payment_modal(self):
        self.driver.find_element(*self.close_card_modal_button).click()

    #Pasos para agregar tarjeta de crédito
    def add_credit_card(self):
        self.driver.implicitly_wait(3)
        self.click_payment_method_input()
        time.sleep(1)
        self.click_credit_card_input()
        self.set_card_number()
        time.sleep(1)
        self.set_card_code()
        time.sleep(.5)
        self.click_remove_focus()
        time.sleep(.5)
        self.click_add_card_button()
        self.close_payment_modal()
        return self.driver.find_element(*self.card_input_value).text

    def check_payment_method(self):
        return self.driver.find_element(*self.card_input_value).text

    def set_driver_message(self):
        self.driver.find_element(*self.driver_message_input).send_keys(data.message_for_driver)

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
        self.driver.WebDriverWait(*self.driver, 50).until(expected_conditions.visibility_of_element_located(*self.order_number))

    def validate_taxi_modal_text(self):
        return self.driver.find_element(*self.taxi_modal_text).text

    def validate_order_data(self):
        return self.driver.find_element(*self.order_number).is_displayed()


class TestUrbanRoutes:

    driver = None
    page = None

    @classmethod
    def setup_class(cls): #AQUÍ EL CÓDIGO ALGO DIFERENTE AL DEL REPOSITORIO, YA QUE UNO DE LOS TUTORES COMENTÓ QUE ESA PLANTILLA NO FUNCIONABA Y DEBÍA MODIFICARSE
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        # Se pasa el objeto 'options' al constructor Chrome
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(data.urban_routes_url)
        cls.page = UrbanRoutesPage(cls.driver)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_1_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        time.sleep(1)

    def test_2_set_comfort_tariff(self):
        page = UrbanRoutesPage(self.driver)
        page.set_comfort_tariff()
        page.check_comfort_button_selected()
        assert 'tcard active' in page.check_comfort_button_selected()
        time.sleep((1))

###ESTA ES LA PRUEBA PARA AGREGAR EL TELÉFONO, PERO AL CORRER EL CÓDIGO LA FUNCIÓN retrieve_phone_code(driver)/
# DE LA PLANTILLA DEL CÓDIGO NO REALIZA NINGUNA ACCIÓN. SI INTRODUZCO OTRO COPY EN EL INPUT SÍ LO CAPTURA.
    #def test_3_set_phone_number(self):
        #page = UrbanRoutesPage(self.driver)
        #page.set_phone_number()
        #page.get_phone_number()
        #assert page.get_phone_number() == data.phone_number


    def test_4_set_credit_card(self):
        page = UrbanRoutesPage(self.driver)
        page.add_credit_card()
        assert page.check_payment_method() == 'Tarjeta'
        time.sleep(1)

    def test_5_set_message_to_driver(self):
        page = UrbanRoutesPage(self.driver)
        page.validate_error_message()
        assert 'La longitud del texto supera los 24 caracteres' in page.get_error_message()
        time.sleep(1)

    def test_6_toggle_blanket_switch(self):
        page = UrbanRoutesPage(self.driver)
        page.toggle_blanket_switch()
        switch_selected = page.validate_blanket_switch()
        assert switch_selected == 'True'
        time.sleep(1)

    def test_7_set_ice_cream(self):
        page = UrbanRoutesPage(self.driver)
        value = page.get_ice_cream_quantity()
        page.add_ice_cream()
        page.get_ice_cream_quantity()
        assert value == '2'
        time.sleep(2)

    def test_8_show_taxi_modal(self):
        page = UrbanRoutesPage(self.driver)
        page.click_reserve_button()
        page.validate_modal_is_visible()
        assert page.validate_modal_is_visible() == True

    def test_9_wait_for_driver_data(self):
        page = UrbanRoutesPage(self.driver)
        time.sleep(35) #Aquí traté de usar la función wait_for_driver_data(self), pero el ejecutar el script no surte ningún efecto
        page.validate_taxi_modal_text()
        assert "El conductor llegará en" in page.validate_taxi_modal_text()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()