import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.urls import Urls
import helpers.utilites as utilites
from helpers.data import *
import helpers.locators as locators

driver = webdriver.Chrome()
driver.get(Urls.url_main_paige)

class TestStellarBurgersCompound:

    #  Переход к разделу "Соусы"
    def test_go_to_section_sauces(self, driver: WebDriver):
        driver = webdriver.Chrome()
        driver.get(Urls.url_main_paige)

        utilites.login(driver)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, locators.m_order_button)))

        driver.find_element(By.XPATH, locators.m_constructor_button).click()
        driver.find_element(By.XPATH, locators.m_sauces_button).click()

        order_button = driver.find_element(By.XPATH, locators.m_t_sauces).text
        assert Urls.url_main_paige == driver.current_url and order_button == 'Соусы'

        driver.quit()

    #  Переход к разделу "Начиники"
    def test_go_to_section_chiefs(self, driver: WebDriver):

        driver = webdriver.Chrome()
        driver.get(Urls.url_main_paige)

        utilites.login(driver)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, locators.m_order_button)))

        driver.find_element(By.XPATH, locators.m_constructor_button).click()
        driver.find_element(By.XPATH, locators.m_filling_button).click()

        chiefs_b = driver.find_element(By.XPATH, locators.m_t_filling).text
        assert Urls.url_main_paige == driver.current_url and chiefs_b == 'Начинки'

        driver.quit()

    # Переход к разделу "Булки"
    def test_go_to_section_buns(self, driver: WebDriver):

        driver = webdriver.Chrome()
        driver.get(Urls.url_main_paige)

        utilites.login(driver)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, locators.m_order_button)))

        driver.find_element(By.XPATH, locators.m_constructor_button).click()
        driver.find_element(By.XPATH, locators.m_filling_button) .click()
        driver.find_element(By.XPATH, locators.m_buns_button).click()

        buns = driver.find_element(By.XPATH, locators.m_t_buns).text
        assert buns == 'Булки'

        driver.quit()
