import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from helpers.urls import Urls

# Создание драйвера Chrome
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1300,1200")
    driver = webdriver.Chrome()
    driver.get(Urls.url_main_paige)
    yield driver
    driver.quit()