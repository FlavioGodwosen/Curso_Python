from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

#Site 1
browser.get("https://gshow.globo.com/")
browser.maximize_window()

sleep(3)

#By LINK_TEXT
browser.find_element(By.LINK_TEXT, "10 eventos em 2024 que você vai acompanhar no gshow")

#Site 2
browser.get("https://www.agorainvestimentos.com.br/login")
browser.maximize_window()

sleep(3)

#By LINK_TEXT
browser.find_element(By.LINK_TEXT, "Primeiro acesso ou Esqueci minha senha")

#Site 3
browser.get('https://www.mercadolivre.com.br/')
browser.maximize_window()

sleep(3)

#By LINK_TEXT
browser.find_element(By.LINK_TEXT, "Compras")

print('Link_Text, Testado com sucesso!')

browser.quit