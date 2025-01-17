
## Sprint_5
Тема "UI тестирование" курс ЯндексПрактикум | Sprint_5
Для тестирования был выбран сервис [Stella Burgers](https://stellarburgers.nomoreparties.site/) 
Космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.
В связи с грядущим релизом был создан чек лист по основному фукнционалу: 

### [Регистрация](tests/test_registration.py) 
- Успешная регистрация
```
def test_registration_correct_email_and_pwd_successful_registration(self, driver: WebDriver)
```

- Поле «Имя» должно быть не пустым
```
def test_registration_name_missing(self, driver: WebDriver)
```

- Пароль - минимум шесть символов
```
def test_registration_correct_email_and_pwd_successful_registration(self, driver: WebDriver)
```

- Ошибка для некорректном email
```
def test_registration_incorrect_email_in_registration_show_error(self, email_list, driver: WebDriver)
```

- Ошибка при некорректном пароле
```
def test_login_incorrect_password_less_six_symbols_show_error(self, driver, password_list)
```

 ### [Авторизация](tests/test_login.py)
- Успешная авторизация 
```
def test_login_correct_email_and_pwd__show_main_page(self, driver: WebDriver)
```

- Авторизация по кнопке «Войти в аккаунт» на главной 
```
 def test_authorization_on_button_Login_to_account(self, driver: WebDriver)
```

- Авторизация по кнопке «Личный кабинет» 
```
def test_login_personal_account_button_show_login_page(self, driver: WebDriver)
```

- Авторизация по кнопке "Войти" в форме регистрации 
```
def test_registration_form_sign_in_button(self, driver: webdriver)
```

- Авторизация по кнопке "Войти" в форме восстановления пароля 
```
def test_login_forgot_password_form_sign_in_button(self, driver: webdriver)
```

### [Личный кабинет](tests/test_lk_profile.py)
- Переход в ЛК по кнопке "Личный кабинет"
```
def test_click_on_personal_account(self)
```

- Переход в конструктор заказов по кнопке "Конструктор"
```
def test_click_on_designer_button(self)
```

- Переход в конструктор заказов по клику на логотип "Stellar Burgers"
```
def test_click_on_logo(self)
```

- Выход из аккаунта по кнопке "Выйти" в ЛК 
```
def test_click_log_out_on_button_log_out(self)
```

### [Раздел «Конструктор»](tests/test_constructor_form.py)
- Переход к разделу "Соусы"
```
def test_go_to_section_sauces(self, driver: WebDriver)
```

- Переход к разделу "Начиники"
```
def test_go_to_section_chiefs(self, driver: WebDriver)
```

- Переход к разделу "Булки"
```
def test_go_to_section_buns(self, driver: WebDriver)
```


Задание со `*` в ./helpers/data.py, класс ValidData. Там рандомайзер для логинов и паролей.
Проверено, что они корректно работают и выдают нужные ошибки.