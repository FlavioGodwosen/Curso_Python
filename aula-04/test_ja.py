import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

@pytest.fixture()
def driver():
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://paulocoliveira.github.io/mypages/jobapplication.html")
  sleep(3)
  yield driver
  driver.quit()

def test_happy_path(driver):
  full_name = driver.find_element(By.CSS_SELECTOR, "form>fieldset>input")
  full_name.send_keys("Flavio Silva de Souza")

  email = driver.find_element(By.XPATH, "//form//fieldset//input[2]")
  email.send_keys("flavio131983@gmail.com")

  phoneNumber = driver.find_element(By.CSS_SELECTOR, "form fieldset input:nth-child(11)")
  phoneNumber.send_keys("11974657709")

  Select(driver.find_element(By.XPATH, "//form/fieldset/select[@id='desiredPosition']")).select_by_visible_text("Developer")
  office = driver.find_element(By.XPATH, "//form//fieldset[2]/input[2]")
  office.click()

  years = driver.find_element(By.CSS_SELECTOR, "form>fieldset:nth-child(3) input[name='experienceYears']")
  years.send_keys("4")

  skills = driver.find_element(By.CSS_SELECTOR, "form fieldset:nth-child(3) input:nth-child(9)")
  skills.click()

  button = driver.find_element(By.CSS_SELECTOR, "button")
  button.click()

  message = driver.find_element(By.ID, "successMessage").text

  sleep(1)

  assert "Submission successful!" == message

  print("Submission successful!")

  sleep(3)
