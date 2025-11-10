from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("usuario","password","debe_funcionar",(
("standard_user","secret_sauce", True),
("admin","1234", False)))
def test_login_validation(login_in_driver, usuario, password,debe_funcionar):
   
    driver = login_in_driver
      # driver
    if debe_funcionar == True:
        assert "/inventory.html" in driver.current_url, "No se redirigio"
    else:
       mensaje_error = LoginPage(driver).obtener_error()
       assert "Epic sadfece" in mensaje_error, "el mensaje no se esta mostrando"