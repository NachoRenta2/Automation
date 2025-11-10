from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #le cambio el nombre para no poner expeted.....
import time
import pytest

@pytest.mark.parametrize("username","password",[
    ("standard","secret"), ("admin", "1234"), ("mod", "123")])


def test_login(username,password):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)# espera implicita, para cinco segundos en cuelquier drive.
    wait = WebDriverWait(driver,10) #espera explicita, para 10 segundos en cada drive
    driver.get("https://www.saucedemo.com/")
    #driver.find_element(By.)# busca elementos

    wait.until(EC.presence_of_element_located((By.ID, "user-Name")))#espera hasta que este visible el campo de usuario

    #localizacion e interaccion de elementos
    driver.find_element(By.ID,"user_name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.quit()