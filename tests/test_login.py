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

class TestStellarBurgersLogin:
    # Успешная авторизация
    def test_login_correct_email_and_pwd__show_main_page(self, driver: WebDriver):
        driver.get(Urls.url_main_paige)

        utilites.login(driver)

        order_button = driver.find_element(By.XPATH, locators.m_order_button).text
        
        assert driver.current_url == Urls.url_main_paige and order_button == FormData.place_an_order
    
    # - Авторизация по кнопке «Войти в аккаунт» на главной 
    def test_authorization_on_button_Login_to_account(self, driver: WebDriver):
        driver.get(Urls.url_main_paige)

        driver.find_element(By.XPATH, locators.m_acc).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locators.l_login_text)))

        driver.find_element(By.XPATH, locators.l_email_field).send_keys(MyData.login)
        driver.find_element(By.XPATH, locators.l_password_field).send_keys(MyData.password)
        driver.find_element(By.XPATH, locators.l_login_button_any_forms).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locators.m_order_button)))

        order_button = driver.find_element(By.XPATH, locators.m_order_button).text
        assert Urls.url_main_paige == driver.current_url and order_button == FormData.place_an_order

    # - Авторизация по кнопке «Личный кабинет» 
    def test_login_personal_account_button_show_login_page(self, driver: WebDriver):
        driver.get(Urls.url_main_paige)

        driver.find_element(By.XPATH, locators.m_profile_button).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locators.l_login_text)))

        driver.find_element(By.XPATH, locators.l_email_field).send_keys(MyData.login)
        driver.find_element(By.XPATH, locators.l_password_field).send_keys(MyData.password)
        driver.find_element(By.XPATH, locators.l_login_button_any_forms).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locators.m_order_button)))

        cab_button = driver.find_element(By.XPATH, locators.m_order_button).text
        assert Urls.url_main_paige == driver.current_url and cab_button == FormData.place_an_order

                
    # - Авторизация по кнопке "Войти" в форме регистрации 
    def test_registration_form_sign_in_button(self, driver: webdriver):
        driver.get(Urls.url_main_paige)

        driver.find_element(By.XPATH, locators.m_profile_button).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locators.l_login_text)))

        driver.find_element(By.XPATH, locators.l_email_field).send_keys(MyData.login)
        driver.find_element(By.XPATH, locators.l_password_field).send_keys(MyData.password)
        driver.find_element(By.XPATH, locators.l_login_button_any_forms).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locators.m_order_button)))

        come_button = driver.find_element(By.XPATH, locators.m_order_button).text
        assert Urls.url_main_paige == driver.current_url and come_button == FormData.place_an_order

    # - Авторизация по кнопке "Войти" в форме восстановления пароля 
    def test_login_forgot_password_form_sign_in_button(self, driver: webdriver):
        driver.get(Urls.url_forgot_password)

        driver.find_element(By.XPATH, locators.p_login_text_with_href).click()

        driver.find_element(By.XPATH, locators.l_email_field).send_keys(MyData.login)
        driver.find_element(By.XPATH, locators.l_password_field).send_keys(MyData.password)
        driver.find_element(By.XPATH, locators.l_login_button_any_forms).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locators.m_order_button)))

        c_button = driver.find_element(By.XPATH, locators.m_order_button).text
        assert Urls.url_main_paige == driver.current_url and c_button == FormData.place_an_order
        

