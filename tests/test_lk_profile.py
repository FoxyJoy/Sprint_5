# - Переход в ЛК по кнопке "Личный кабинет"
# - Переход в конструктор заказов по кнопке "Конструктор"
# - Переход в конструктор заказов по клику на логотип "Stellar Burgers"
# - Выход из аккаунта по кнопке "Выйти" в ЛК 

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.urls import Urls
import helpers.utilites as utilites
import helpers.locators as locators

class TestStellarBurgersPersonalAccount:
    # Открыть личный кабинет 
    def test_click_on_personal_account(self):

        driver = webdriver.Chrome()
        driver.get(Urls.url_main_paige)
        
        utilites.login(driver)
        
        driver.find_element(By.XPATH, locators.m_profile_button).click()

        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, locators.lk_info_message)))
        profile = driver.find_element(By.XPATH, locators.lk_history_message).text

        assert Urls.url_profile == driver.current_url and profile == 'История заказов'

        driver.quit()


    # Переход в конструктор заказов по кнопке "Конструктор"
    def test_click_on_designer_button(self):
        driver = webdriver.Chrome()
        driver.get(Urls.url_main_paige)

        utilites.login(driver)

        driver.find_element(By.XPATH, locators.m_constructor_button).click()

        WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, locators.m_order_button)))
        profile = driver.find_element(By.XPATH, locators.m_order_button).text

        assert Urls.url_main_paige == driver.current_url and profile == 'Оформить заказ'

        driver.quit()


    # Переход в конструктор заказов по клику на логотип "Stellar Burgers"
    def test_click_on_logo(self):
        driver = webdriver.Chrome()
        driver.get(Urls.url_main_paige)

        utilites.login(driver)

        driver.find_element(By.XPATH, locators.m_logo)

        h1_t = driver.find_elements(By.XPATH, locators.lk_logo_pick)
        assert len(h1_t) > 0 and h1_t[0].text == 'Соберите бургер'

        driver.quit()


    # Выход из аккаунта по кнопке "Выйти" в ЛК 
    def test_click_log_out_on_button_log_out(self):
        driver = webdriver.Chrome()
        driver.get(Urls.url_main_paige)

        utilites.login(driver)

        driver.find_element(By.XPATH, locators.m_profile_button).click()
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, locators.lk_history_message)))

        driver.find_element(By.XPATH, locators.lk_logout_button).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locators.l_login_button_any_forms)))
        
        assert driver.current_url == Urls.url_login and driver.find_element(By.XPATH, locators.l_element_with_login_text).text == 'Вход'

        driver.quit()
