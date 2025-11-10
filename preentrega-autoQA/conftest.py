import pytest
from selenium import webdriver
#from utils import login
from pages.login_page import LoginPage

@pytest.fixture
    
def driver():
    driver = webdriver.Chrome()
    yield driver #puede devolver un valor de test.
    # ejecuta lo que sigue sin saber lo anterior
    driver.quit()

@pytest.fixture
def login_in_driver(driver,usuario,password):
    LoginPage(driver).abrir_pagina().login_completo(usuario, password)
#@pytest.fixture
#def login_in_driver(driver): #
 #   login(driver) #llamamos a la funcion login pasandole el driver
 #   return driver# estariamos globalizando el login-in_driver, es decir que login sea usable sin importacion
            #
 # si tengo varios usuarios hay que usar el markparametrize
 # si quiero probar login incorrecto tendria que hacer otra funcion y ver los errores