from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    #driver.find_element(By.)# busca elementos

    #localizacion e interaccion de elementos
    driver.find_element(By.ID,"user_name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.quit()


