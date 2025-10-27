import pytest
from selenium import webdriver
from utils import login


@pytest.fixture
    
def driver():
    driver = webdriver.Chrome()
    yield driver #puede devolver un valor de test.
    # ejecuta lo que sigue sin saber lo anterior
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver
 