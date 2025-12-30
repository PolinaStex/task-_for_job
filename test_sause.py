import allure
import pytest
from selenium import webdriver
from sause_page import LoginPage_1,LoginPage_2,LoginPage_3,LoginPage_4,LoginPage_5

@pytest.fixture()
@allure.title("Тестирование интернет-магазина")
@allure.description("Тест проверяет корректную работу интернет-магазина")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_page():
    driver=webdriver.Firefox()
    driver.implicitly_wait(20)
    driver.maximize_window()
    with allure.step("Открытие страницы кулькулятора"):
        driver.get("https://www.saucedemo.com/")
    with allure.step("Заполнить поля на странице"):
        LoginPage_1.login_succ()
def test_incorrect_login():
    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    driver.maximize_window()
    with allure.step("Открытие страницы кулькулятора"):
        driver.get("https://www.saucedemo.com/")
    with allure.step("Заполнить поля на странице"):
        LoginPage_2.login_unsucc()
def test_locked_out_user():
    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    driver.maximize_window()
    with allure.step("Открытие страницы кулькулятора"):
        driver.get("https://www.saucedemo.com/")
    with allure.step("Заполнить поля на странице"):
        LoginPage_3.locked_out_user()
def test_empty_login():
    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    driver.maximize_window()
    with allure.step("Открытие страницы кулькулятора"):
        driver.get("https://www.saucedemo.com/")
    with allure.step("Заполнить поля на странице"):
        LoginPage_4.empty_login()
def performance_glitch_user():
    driver = webdriver.Firefox()
    driver.implicitly_wait(20)
    driver.maximize_window()
    with allure.step("Открытие страницы кулькулятора"):
        driver.get("https://www.saucedemo.com/")
    with allure.step("Заполнить поля на странице"):
        LoginPage_5.performance_glitch_user()

