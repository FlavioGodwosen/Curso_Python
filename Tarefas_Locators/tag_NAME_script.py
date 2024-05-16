from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

#Site 1
browser.get("https://gshow.globo.com/")
browser.maximize_window()

sleep(3)

#By TAG_NAME
browser.find_elements(By.TAG_NAME, "a")

#Site 2
browser.get("https://www.agorainvestimentos.com.br/login")
browser.maximize_window()

sleep(3)

#By TAG_NAME
browser.find_elements(By.TAG_NAME, "a")

#Site 3
browser.get('https://www.mercadolivre.com.br/')
browser.maximize_window()

sleep(3)

#By TAG_NAME
assert browser.find_elements(By.TAG_NAME, "a")

print('TAG_NAME, Testado com sucesso!')

browser.quit