from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from faker import faker

#inicializamons
faker = faker()

@pytest.mark.parametrize("usuario, password, debe_funcionar",[
    (faker.user_name(),faker.password(), False),
    (faker.user_name(),faker.password(), False) #("standard_user","secret_sauce"),
])
def test_login_validation(login_in_driver, usuario, password, debe_funcionar):
      driver = login_in_driver
      # driver
if debe_funcionar == True:
        assert "/inventory.html" in driver.current_url, "No se redirigio"
elif debe_funcionar == True:
       mensaje_error = LoginPage(driver).obtener_error()
       assert "Epic sadface" in mensaje_error, "el mensaje no se esta mostrando"