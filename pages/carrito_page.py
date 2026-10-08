from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

class CarritoPage:
    PRODUCTOS = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def obtener_nombres_productos(self):
        def leer_nombres(driver):
            try:
                nombres = [
                    elemento.text
                    for elemento in driver.find_elements(*self.PRODUCTOS)
                ]
                return nombres if nombres and all(nombres) else False
            except StaleElementReferenceException:
                # SauceDemo puede volver a renderizar el carrito durante la lectura.
                return False

        return WebDriverWait(self.driver, 10).until(leer_nombres)
