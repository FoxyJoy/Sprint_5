import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.urls import Urls
from helpers.data import *
import helpers.locators as locators

class TestStellarBurgersRegistration:
    # При успешной регистрации перебрасывает на страницу входа
    def test_registration_correct_email_and_pwd_successful_registration(self, driver: WebDriver):

        driver.get(Urls.url_register)

        driver.find_element(By.XPATH, locators.r_name_field).send_keys(MyData.user_name)
        driver.find_element(By.XPATH, locators.r_email_field).send_keys(MyData.login)
        driver.find_element(By.XPATH, locators.r_password_field).send_keys(MyData.password)
        driver.find_element(By.XPATH, locators.r_register_button).click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locators.l_element_with_login_text)))
        
        assert driver.current_url == Urls.url_login and driver.find_element(By.XPATH, locators.l_element_with_login_text).text == FormData.enter

    # Регистрации при вводе некорректного пароля
    def test_registration_incorrect_password(self, driver: WebDriver):
        driver.get(Urls.url_register)

        driver.find_element(By.XPATH, locators.r_name_field).send_keys(MyData.user_name)
        driver.find_element(By.XPATH, locators.r_email_field).send_keys(MyData.login)
        driver.find_element(By.XPATH, locators.r_password_field).send_keys(MyData.incorrect_pass)
       
        driver.find_element(By.XPATH, locators.r_register_button).click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, locators.r_error_message).text == FormData.incorrect_pass

    # При пустом поле Имя ничего не происходит: ошибки и перехода на страницу входа нет 
    def test_registration_name_missing(self, driver: WebDriver):

        driver.get(Urls.url_register)

        driver.find_element(By.XPATH, locators.r_name_field).send_keys(MyData.user_name)
        driver.find_element(By.XPATH, locators.r_email_field).send_keys(MyData.login)
       
        driver.find_element(By.XPATH, locators.r_register_button).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, locators.r_register_button)))

        assert driver.current_url == Urls.url_register

    # При некорректном email появляется ошибка, что пользователь уже существует 
    @pytest.mark.parametrize('email_list', ['Olesya_Sizova_13a_qa_134@yandex.ru', 'Olesya_Sizova_13a_qa_133yandex.ru', 'Olesya_Sizova_13a_qa_132@yandex.ru'])
    def test_registration_incorrect_email_in_registration_show_error(self, email_list, driver: WebDriver):

        driver.get(Urls.url_register)
 
        driver.find_element(By.XPATH, locators.r_name_field).send_keys(MyData.user_name)
        driver.find_element(By.XPATH, locators.r_email_field).send_keys(email_list)
        driver.find_element(By.XPATH, locators.r_password_field).send_keys(MyData.password)
        driver.find_element(By.XPATH, locators.r_register_button).click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, locators.r_error_message_2)))

        error_message = driver.find_element(By.XPATH, locators.r_error_message_2).text
        assert error_message == FormData.user_exist

    # При вводе некорректного пароля, отображает ошибку 'Некорректный пароль
    @pytest.mark.parametrize('password_list', ['qwert', '12345', '12qw3'])
    def test_login_incorrect_password_less_six_symbols_show_error(self, driver, password_list):

        driver.get(Urls.url_register)

        driver.find_element(By.XPATH, locators.r_name_field).send_keys(MyData.user_name)
        driver.find_element(By.XPATH, locators.r_email_field).send_keys(MyData.login)
        driver.find_element(By.XPATH, locators.r_password_field).send_keys(password_list)

        driver.find_element(By.XPATH, locators.r_register_button).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, locators.r_error_message)))
        error_message = driver.find_element(By.XPATH, locators.r_error_message).text

        assert error_message == FormData.incorrect_pass
