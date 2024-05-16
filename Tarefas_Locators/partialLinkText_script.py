from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

#Site 1
browser.get("https://gshow.globo.com/")
browser.maximize_window()

sleep(3)

#By PARTIAL_LINK_TEXT
browser.find_element(By.PARTIAL_LINK_TEXT, "10 eventos em 2024 ")

#Site 2
browser.get("https://www.agorainvestimentos.com.br/login")
browser.maximize_window()

sleep(3)

#By PARTIAL_LINK_TEXT
browser.find_element(By.PARTIAL_LINK_TEXT, "Primeiro acesso ")

#Site 3
browser.get('https://www.mercadolivre.com.br/')
browser.maximize_window()

sleep(3)

#By PARTIAL_LINK_TEXT
browser.find_element(By.PARTIAL_LINK_TEXT, "Comp")

print('PARTIAL_LINK_TEXT, Testado com sucesso!')

browser.quit