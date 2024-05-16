from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_principal_scenario(driver):
    username = driver.find_element(By.NAME, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.ID, "login-button")
    button.click()

    products = driver.find_elements(By.XPATH, "//button[contains(@data-test, 'add-to-cart-')]")
   
    for product in products:
        product.click()
    
    badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
    assert badge == "6"

    cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    cart.click()

    product_to_remove = driver.find_element(By.ID, "remove-sauce-labs-bike-light")
    product_to_remove.click()

    badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
    assert badge == "5"

    checkout_button = driver.find_element(By.NAME, "checkout")
    checkout_button.click()

    first_name = driver.find_element(By.NAME, "firstName")
    first_name.send_keys("Flavio")

    last_name = driver.find_element(By.NAME, "lastName")
    last_name.send_keys("Silva")

    postal_code = driver.find_element(By.NAME, "postalCode")
    postal_code.send_keys("06365-210")

    continue_button = driver.find_element(By.CLASS_NAME, "submit-button")
    continue_button.click()

    finish_button = driver.find_element(By.CSS_SELECTOR, "#finish")
    finish_button.click()

    confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header").text
    assert confirmation_message == "Thank you for your order!"
    
    print("Teste 1 - Projeto fluxo feliz, com sucesso!")
  
    #Acessar Site - Erro nos campos de dados
def test_problem_user(driver):
    username = driver.find_element(By.XPATH, "//form//div/input[1]")
    username.send_keys("problem_user")
    
    password = driver.find_element(By.XPATH, "//form//div[2]/input[1]")
    password.send_keys("secret_sauce")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
    login_button.click()
    
    # Add Produtos
    add_product = driver.find_element(By.CSS_SELECTOR, "body>div:nth-child(2) button:nth-child(2)")
    add_product.click()
    
    # Clicar no carrinho
    carrinho = driver.find_element(By.XPATH, "//body//div/a/span")
    carrinho.click()
    
    # Clicar em checkout
    checkout_button = driver.find_element(By.NAME, "checkout")
    checkout_button.click()
    
    # Preencher os dados
    firstname = driver.find_element(By.ID, "first-name")
    firstname.send_keys("Manu")
    
    lastname = driver.find_element(By.ID, "last-name")
    lastname.send_keys("Martins de Souza")
    
    postalcode = driver.find_element(By.ID, "postal-code")
    postalcode.send_keys("06365210")
    
    
    continue_button = driver.find_element(By.CSS_SELECTOR, "#continue")
    continue_button.click()
    
    # Validando botão de Erro
    driver.find_element(By.CLASS_NAME, "error-button")
    
    print('Teste 2 - Erro nos campos de first e last name!')
   
    
   
    #Acessar Site - Realizar Reset
def test_reset(driver):
    username = driver.find_element(By.XPATH, "//form//div/input[1]")
    username.send_keys("standard_user")
    
    password = driver.find_element(By.XPATH, "//form//div[2]/input[1]")
    password.send_keys("secret_sauce")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
    login_button.click()
    
    
    
    #Add Produtos
    products = driver.find_elements(By.XPATH, "//button[contains(@data-test, 'add-to-cart-')]")
   
    for product in products:
        product.click()
    
    badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
    assert badge == "6"
    
      
    #Clicar no Hamburguer
    button = driver.find_element(By.CSS_SELECTOR, "body>div:nth-child(2) button")
    button.click()
    
    #Clicar em Reset App State
    reset = driver.find_element(By.CSS_SELECTOR, "div>nav>a:nth-child(4)")
    reset.click
    
    print('Teste 3 - Reset, com sucesso!') 
        
    
   #Acessar Site - Realizar Logout
def test_Logout(driver):
    username = driver.find_element(By.XPATH, "//form//div/input[1]")
    username.send_keys("standard_user")
    
    password = driver.find_element(By.XPATH, "//form//div[2]/input[1]")
    password.send_keys("secret_sauce")
    
    login_button = driver.find_element(By.CSS_SELECTOR, "#login-button")
    login_button.click() 
    
    #Clicar no Hamburguer
    hamburguer_button = driver.find_element(By.CSS_SELECTOR, "body>div:nth-child(2) button")
    hamburguer_button.click()
    
    #Clicar em Logout
    link_logout = driver.find_element(By.CSS_SELECTOR, "div>nav>a:nth-child(3)")
    link_logout.click   
     
    print('Teste 4 - Logout, com sucesso!')
    
    
def test_sorting(driver):
    username = driver.find_element(By.NAME, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.ID, "login-button")
    button.click()

    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_visible_text("Price (low to high)")

    

    products = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    prices = []

    for product in products:
        price = product.text
        price = price.replace("$", "")
        prices.append(float(price))
    
    sorted_prices = sorted(prices)

    assert prices == sorted_prices    
    
    print("Teste 5 - Ordenação, com sucesso! ")
    
       
    
def test_total_price(driver):
    username = driver.find_element(By.NAME, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce")

    button = driver.find_element(By.ID, "login-button")
    button.click()

    products = driver.find_elements(By.XPATH, "//button[contains(@data-test, 'add-to-cart-')]")
   
    for product in products:
        product.click()
    
    product_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    total_sum = 0

    for item in product_prices:
        price = item.text
        price = price.replace("$", "")
        total_sum = total_sum + float(price)
    
    cart = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    cart.click()

    checkout_button = driver.find_element(By.NAME, "checkout")
    checkout_button.click()

    first_name = driver.find_element(By.NAME, "firstName")
    first_name.send_keys("Lucas")

    last_name = driver.find_element(By.NAME, "lastName")
    last_name.send_keys("Martins")

    postal_code = driver.find_element(By.NAME, "postalCode")
    postal_code.send_keys("06365-210")

    continue_button = driver.find_element(By.CLASS_NAME, "submit-button")
    continue_button.click()

    total_price = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
    total = total_price.split("$")[1]
    total = float(total)
    
    assert total == total_sum

    print('Teste 6 - Validando preço total com sucesso!')
        
        