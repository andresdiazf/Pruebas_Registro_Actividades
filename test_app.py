from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
url = "http://localhost:3000"
driver.get(url)
time.sleep(2)  # se debe configurar tiempo para evitar errores de ejecución


# Prueba 1 - Home: Ir al home y clic en boton iniciar sesión.

def test_register():
    btn_inicio = driver.find_element(
        By.XPATH, '//*[@id="root"]/main/div/div/a')
    btn_inicio.click()
    time.sleep(3)
    assert True

# Prueba 2 - login: Registrar Usuario.
    username = driver.find_element(By.XPATH, '//*[@id="username"]/input')
    username.send_keys("edwin.pena@grupo15.edu")
    time.sleep(2)
    assert True

# Prueba 3 - login: Registrar Contraseña
    password = driver.find_element(By.XPATH, '//*[@id="password"]/input')
    password.send_keys("12345678")
    time.sleep(2)
    assert True

# Prueba 4 - login: Activar boton enviar
    btn_enviar_login = driver.find_element(
        By.XPATH, '//*[@id="navbarNav"]/ul/li[3]/a')
    btn_enviar_login.click()
    time.sleep(2)
    assert True

# prueba 5 - register:  registrar actividad
    register_activiti = driver.find_element(
        By.XPATH, '//*[@id="root"]/main/div/form/div/div/div[1]/label/input')
    register_activiti.send_keys("actividad de prueba final")
    time.sleep(2)
    assert True

# prueba 6 - register:  registrar fecha y hora
    register_date_hour = driver.find_element(
        By.XPATH, '//*[@id="root"]/main/div/form/div/div/div[2]/label/input')
    register_date_hour.send_keys("05/05/2024")
    register_date_hour.send_keys(Keys.TAB)
    time.sleep(2)
    register_date_hour.send_keys("12:25")
    time.sleep(2)
    register_date_hour.send_keys(Keys.ARROW_UP)
    time.sleep(2)
    assert True


# Prueba No 7 - send register: Activar boton enviar registro de actividades
    btn_enviar_register = driver.find_element(
        By.XPATH, '//*[@id="root"]/main/div/form/div/div/button')
    btn_enviar_register.click()
    time.sleep(2)

    alert = driver.switch_to.alert
    alert.accept()
    time.sleep(2)
    assert True

# prueba No 8  - Activities: consultar y ver registros de actividades


def test_consult():
    btn_consult_page = driver.find_element(
        By.XPATH, '//*[@id="navbarNav"]/ul/li[4]/a')
    btn_consult_page.click()
    time.sleep(2)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())
    wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/main/div/div/a]')))
    driver.switch_to.alert.accept()

    time.sleep(4)
    # alert = driver.switch_to.alert
    # alert.accept()

    assert True

    # cerrar el nevegador
    # driver.quit()
