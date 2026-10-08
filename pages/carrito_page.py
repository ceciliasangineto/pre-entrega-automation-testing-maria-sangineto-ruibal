from selenium.webdriver.common.by import By

class CarritoPage:
    PRODUCTOS = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def obtener_nombres_productos(self):
        elementos = self.driver.find_elements(*self.PRODUCTOS)
        return [elemento.text for elemento in elementos]