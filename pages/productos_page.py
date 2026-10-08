from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductosPage:
    LOGO = (By.CLASS_NAME, "app_logo")
    LISTA_PRODUCTOS = (By.CLASS_NAME, "inventory_list")
    MENU_DESPEGABLE = (By.CLASS_NAME, "product_sort_container")
    BOTON_AGREGAR = (By.ID, "add-to-cart-sauce-labs-backpack")
    CONTADOR_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
    CARRITO = (By.CLASS_NAME, "shopping_cart_link")


    def __init__(self, driver):
        self.driver = driver

    def obtener_titulo(self):
        return self.driver.title

    def obtener_texto_logo(self):
        return self.driver.find_element(*self.LOGO).text

    def lista_productos_visible(self):
        return self.driver.find_element(*self.LISTA_PRODUCTOS).is_displayed()

    def menu_desplegable_visible(self):
        return self.driver.find_element(*self.MENU_DESPEGABLE).is_displayed()

    def agregar_producto_al_carrito(self):
        boton = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BOTON_AGREGAR)
        )
        boton.click()

    def obtener_cantidad_en_carrito(self):
        contador = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CONTADOR_CARRITO)
        )
        return int(contador.text)

    def abrir_carrito(self):
        self.driver.find_element(*self.CARRITO).click()

