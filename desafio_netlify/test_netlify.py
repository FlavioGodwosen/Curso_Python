import pytest
from selenium import webdriver
from pages.base_page import BasePage
from desafio_netlify.pages.pesquisauser_page import PesquisaUserPage
from desafio_netlify.pages.username_page import NomeUserPage
from config.webdriver_singleton import WebDriverSingleton


@pytest.fixture()
def driver():
    driver = WebDriverSingleton.get_instance()
    BasePage(driver).go_to_site()
    yield driver

@pytest.fixture(scope="session", autouse=True)
def close_browser():
    yield
    WebDriverSingleton.quit_instance()

def test_pesquisa_user(driver):
    pesquisa_page = PesquisaUserPage(driver)
    pesquisa_page.search_user("FlavioGodwosen")
  
def test_user_name(driver):
    username_page = NomeUserPage(driver)
    username_page.follow_user("Flavio Silva de Souza") 