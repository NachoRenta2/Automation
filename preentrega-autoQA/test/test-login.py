from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com")# direccion donde buscar..
        driver.find_element(By.ID,"user-name").send_keys("standard_user")#busca un elemento en una web con determinado ID
        driver.find_element(By.ID,"password").send_keys("secret_sauce")#ademas de buscar en este caso un campo, le establece valores
        driver.find_element(By.ID,"login-button").click()#hago click

   
        
        assert "/inventory.html" in driver.current_url, "No se redirigio correctamente al inventario"

        print("Login exitoso y validado")
        
    except Exception as e:
        print(f"Error en test login: {e}")
        raise #resalta el error.
    finally:
        driver.quit()
        #para generar reporte html
        #py -m pytest test-login.py -v(detallado) --html=(ruta del reporte)\reporte.html test-login.py
