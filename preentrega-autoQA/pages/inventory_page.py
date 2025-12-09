from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InventoryPage:
    #selectores
    _INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    _ADD_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    _CART_COUNT = (By.CLASS_NAME, "shopping_cart_badge")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _CART_LINK = (By.CLASS_NAME, " shopping_cart_link")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait (driver, 10)
    
    def obtener_todos_los_item(self):
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        #productos = self.wait.until(EC.visibility_of_all_elements_located(*self._INVENTORY_ITEMS))
        # el * desempaqueta los datos que trae visibility
        #return productos #captura los productos y los acomoda como una lista por el *
        productos = self.driver.find_elements(*self._INVENTORY_ITEMS)
        # conviene esta pq me garantizo que se cumple la espera, se obtienen los productos desempaquetados
        return productos
    
    def obtener_nombres_productos(self):
        productos = self.driver.find_elementos(*self._ITEM_NAME)
        return [producto_nombre.text for producto_nombre in productos]
    #recorremos cada producto por cada vuelta dentro de productos y los guardamos, lista por comprension

    def agregar_primer_producto(self):
        producto = self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))

        primer_boton_producto = producto[0].find_element(self._ADD_TO_CART_BUTTON)
        primer_boton_producto.click()
    
    def agregar_producto_por_nombre(self,nombre_producto):
        
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        productos = self.obtener_todos_los_producos}

        for productos in productos
            nombre = prodcto.find_element(By.CLASSS_NAME, self._ITEM_NAME).tect

            if nombre.strip().lower == nombre_producto.strip():
                boton = producto.find_element(self. _ADD_TO CART)