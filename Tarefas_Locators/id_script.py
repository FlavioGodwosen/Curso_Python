from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
#Site 1
browser.get("https://www.bvb.de/")
browser.maximize_window()

sleep(3)

#By ID
browser.find_element(By.ID, "logo")

#Site 2
browser.get("https://www.agorainvestimentos.com.br/login")
browser.maximize_window()

sleep(3)

#By ID
browser.find_element(By.ID, "CPFCNPJ")

#Site 3
browser.get("https://www.casasbahia.com.br/")
browser.maximize_window()

sleep(3)

#By ID
browser.find_element(By.ID, "visualwebsite-optimizer")

print('ID, Testado com sucesso!')

browser.quit()