from time import sleep
from selenium import webdriver

browser= webdriver.Chrome()

browser.get("https://www.uol.com.br/")
browser.maximize_window()
sleep(5)

title = browser.title

print(title)

browser.quit()