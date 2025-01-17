from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from helpers.urls import Urls
from helpers.data import MyData
import helpers.locators as locators

# Войти в аккаунт
def login(driver):
    driver.get(Urls.url_login)

    driver.find_element(By.XPATH, locators.r_email_field).send_keys(MyData.login)
    driver.find_element(By.XPATH, locators.r_password_field).send_keys(MyData.password)
    driver.find_element(By.XPATH, locators.l_login_button_any_forms).click()
 
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locators.m_order_button)))