from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://paulocoliveira.github.io/mypages/validation/index.html")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

#Atributo pode ser alterado durante execução, esse teste pode ser usado para esse tipo de situação  
    
def test_get_attribute(driver):
    title = driver.find_element(By.ID, "title")
    value = title.get_attribute("data-test")
    assert value == "testValue"  
      
#Clicar e receber um "TRUE" ou não clicar e receber um "FALSE"
def test_is_displayed(driver):
    driver.find_element(By.ID, "toggleButton").click()
    hidden_message = driver.find_element(By.ID, "hiddenMessage")
    assert hidden_message.is_displayed()    
    
def test_is_enabled(driver):
    input_field = driver.find_element(By.ID, "inputField")
    assert input_field.is_enabled()

#Validando e clicando no checkBox    
def test_get_property(driver):
    checkbox = driver.find_element(By.ID, "testCheckbox")
    assert checkbox.get_property("checked") == True
    checkbox.click()
    assert checkbox.get_property("checked") == False
    
#Validando e clicando no checkBox      
def test_is_selected(driver):
    checkbox = driver.find_element(By.ID, "testCheckbox")
    assert checkbox.is_selected() == True
    checkbox.click()
    assert checkbox.is_selected() == False, "Checkbox should be selected"      

#Validando cores de um botão    
def test_value_of_css_property(driver):
    button = driver.find_element(By.ID, "toggleButton")
    assert button.value_of_css_property("color") == "rgba(255, 255, 255, 1)"       
    
#Vou validar o tamanho de um componente ou elemento
def test_get_size(driver):
    button = driver.find_element(By.ID, "testButton")
    size = button.size
    assert size["width"] == 1310 and size["height"] == 38, "Button size is not 1310 x 38"
    
#Validar posição da pagina, posição do elemento na pagina
def test_get_location(driver):
    button = driver.find_element(By.ID, "testButton")
    location = button.location
    assert location["x"] == 28 and location["y"] == 286, "Button location is not x = 28 and y = 286"
    
#Validar qual tipo de elemento     
def test_tag_name(driver):
    button = driver.find_element(By.ID, "testButton")
    assert button.tag_name == "button"