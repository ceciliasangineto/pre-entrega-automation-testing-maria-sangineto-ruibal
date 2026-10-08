from pages.productos_page import ProductosPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.productos_page import ProductosPage
from pages.carrito_page import CarritoPage

def test_titulo_de_pagina(logged_in_driver):
    pagina = ProductosPage(logged_in_driver)
    assert pagina.obtener_titulo() == "Swag Labs"


def test_logo_visible_y_correcto(logged_in_driver):
    pagina = ProductosPage(logged_in_driver)
    assert pagina.obtener_texto_logo() == "Swag Labs"


def test_lista_de_productos_visible(logged_in_driver):
    pagina = ProductosPage(logged_in_driver)
    assert pagina.lista_productos_visible()

def test_menu_desplegable_visible(logged_in_driver):
    pagina = ProductosPage(logged_in_driver)
    assert pagina.menu_desplegable_visible()

def test_agregar_producto_incrementa_contador(logged_in_driver):
    pagina = ProductosPage(logged_in_driver)
    pagina.agregar_producto_al_carrito()
    assert pagina.obtener_cantidad_en_carrito() == 1


def test_producto_agregado_aparece_en_carrito(logged_in_driver):
    productos = ProductosPage(logged_in_driver)

    productos.abrir_carrito()

    carrito = CarritoPage(logged_in_driver)

    assert "Sauce Labs Backpack" in carrito.obtener_nombres_productos()