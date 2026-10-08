# QA Automation Pre Entrega

Automatización web de SauceDemo con Selenium, pytest y el patrón Page Object Model (POM).

## Requisitos

- Python 3.10 o posterior
- Google Chrome
- `pytest`
- `selenium`

Instala las dependencias:

```bash
python -m pip install pytest selenium
```

## Ejecutar las pruebas

Desde la raíz del proyecto:

```bash
python -m pytest -v
```

El fixture `logged_in_driver` de `tests/conftest.py` inicia sesión en SauceDemo y comparte el navegador durante la ejecución de pytest.

## Estructura

```text
pages/   Objetos de página y acciones
tests/   Pruebas y fixture de Selenium
```
