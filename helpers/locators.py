# class MainPage: 
m_profile_button = ".//p[text()='Личный Кабинет']"
m_acc = ".//button[text()='Войти в аккаунт']"
m_order_button = ".//button[text()='Оформить заказ']"
m_constructor_button = ".//p[text()='Конструктор']"
m_logo = ".//div[@class='AppHeader_header__logo__2D0X2']"
m_sauces_button = ".//span[text()='Соусы']/parent::*"
m_t_sauces = ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']"
m_buns_button = ".//span[text()='Булки']/parent::*"
m_t_buns = ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']"
m_filling_button = ".//span[text()='Начинки']/parent::*"
m_t_filling =  ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']"

# class LoginAuth:
l_login_text = ".//h2[text()='Вход']"
l_login_button_any_forms = ".//button[text()='Войти']"
l_email_field = ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']"
l_password_field = ".//input[@type='password' and @name='Пароль']"
l_element_with_login_text = ".//*[text() = 'Вход']"

# class RegistrationAuth:
r_name_field = ".//label[text()='Имя']//parent::*/input[@type='text' and @name='name']"
r_email_field = ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']"
r_password_field = ".//input[@type='password' and @name='Пароль']"
r_register_button = ".//button[text()='Зарегистрироваться']"
r_error_message = ".//p[@class='input__error text_type_main-default']"
r_error_message_2 = ".//div[@class='Auth_login__3hAey']/p[@class='input__error text_type_main-default']"

# class PasswordAuth:
p_login_text_with_href = ".//a[text()='Войти']"

# class LKProfile:
lk_logout_button = ".//button[text()='Выход']"
lk_info_message = ".//p[contains(text(),'персональные данные')]"
lk_history_message = ".//a[text()='История заказов']"
lk_logo_pick = ".//h1"