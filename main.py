import time
import data
from selenium import webdriver
from pages import UrbanRoutesPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestUrbanRoutes:

    driver = None
    page = None

    @classmethod
    def setup_class(cls): #AQUÍ EL CÓDIGO ALGO DIFERENTE AL DEL REPOSITORIO, YA QUE UNO DE LOS TUTORES COMENTÓ QUE ESA PLANTILLA NO FUNCIONABA Y DEBÍA MODIFICARSE
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
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
    def test_3_set_phone_number(self):
        page = UrbanRoutesPage(self.driver)
        page.set_phone_number()
        page.get_phone_number()
        assert page.get_phone_number() == data.phone_number


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