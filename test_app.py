from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
url = "http://localhost:3000"
driver.get(url)
time.sleep(2)


# Prueba 1 - Home: Ir al home y clic en boton iniciar sesión.

def test_register():
    btn_inicio = driver.find_element(
        By.XPATH, '//*[@id="root"]/main/div/div/a')
    btn_inicio.click()
    time.sleep(5)

# Prueba 2 - login: Registrar Usuario.
    username = driver.find_element(By.XPATH, '//*[@id="username"]/input')
    username.send_keys("prueba@username.com")
    time.sleep(3)

# Prueba 3 - login: Registrar Contraseña
    password = driver.find_element(By.XPATH, '//*[@id="password"]/input')
    password.send_keys("12345678")
    time.sleep(3)

# Prueba 4 - login: Activar boton enviar
    btn_enviar = driver.find_element(
        By.XPATH, '//*[@id="root"]/main/div/div/div/div/div/div/div[2]/div/form/button')
    btn_enviar.click()
    time.sleep(5)
