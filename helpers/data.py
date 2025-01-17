import random

class ValidData:
    user_name = 'Test test'
    login = f"Test_test{random.randint(10, 999)}@yandex.ru"
    password = f"{random.randint(100, 999)}{random.randint(100, 999)}"

class MyData:
    user_name = 'Olesya Sizova'
    login = 'Olesya_Sizova_13a_qa_134@yandex.ru'
    password = 'Q123werty123Q'
    incorrect_pass = '12345'
    incorrect_user_name = ''