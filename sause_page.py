import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=webdriver.Firefox()
driver.maximize_window()

@allure.title("Страница интернет-магазина")
@allure.feature("READ")
@allure.description("Заполнение полей и нажимание кнопко на странцие интернет-магазина")
@allure.severity("blocker")
class LoginPage_1:
    def login_succ(self,driver,param:str):
       """
            Эта функция находит поля страницы по локатору и вводит заданные параметры в каждое поле
       """
        with allure.step("Найти элемент на странице"):
            user_name=driver.find_element(By.CSS_SELECTOR, '#user-name')
        with allure.step("Отправить значение логина"):
            user_name=driver.send_keys('standard_user')
        with allure.step("Найти элемент на странице"):
            password=driver.find_element(By.CSS_SELECTOR, '#password')
        with allure.step("Отправить значение пароля"):
            password=driver.send_keys('secret_sauce')
            driver.implicitly_wait(4)
        with allure.step("Найти элемент на странице и нажать на него"):
            login=driver.find_element(By.CSS_SELECTOR, '#login-button').click()
    driver.implicitly_wait(4)
class LoginPage_2:
    def login_unsucc(self,driver,param:str):
        with allure.step("Найти элемент на странице"):
            user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
        with allure.step("Отправить значение логина"):
            user_name = driver.send_keys('standard_user')
        with allure.step("Найти элемент на странице"):
            password = driver.find_element(By.CSS_SELECTOR, '#password')
        with allure.step("Отправить значение пароля"):
            password = driver.send_keys('sec_sauce')
        driver.implicitly_wait(4)
        with allure.step("Найти элемент на странице и нажать на него"):
            login = driver.find_element(By.CSS_SELECTOR, '#login-button').click()
            driver.implicitly_wait(4)

class LoginPage_3:
    def locked_out_user(self,driver,param:str):
        with allure.step("Найти элемент на странице"):
            user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
        with allure.step("Отправить значение логина"):
            user_name = driver.send_keys('standard_user')
        with allure.step("Найти элемент на странице"):
            password = driver.find_element(By.CSS_SELECTOR, '#password')
        with allure.step("Отправить значение пароля"):
            password = driver.send_keys('secret_sauce')
            driver.implicitly_wait(4)
        with allure.step("Найти элемент на странице и нажать на него"):
            login = driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        driver.implicitly_wait(4)

class LoginPage_4:
    def empty_login (self,driver,param:str):
        with allure.step("Найти элемент на странице"):
            user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
        with allure.step("Отправить значение логина"):
            user_name = driver.send_keys('standard_user')
        with allure.step("Найти элемент на странице"):
            password = driver.find_element(By.CSS_SELECTOR, '#password')
        with allure.step("Отправить значение пароля"):
            password = driver.send_keys('secret_sauce')
        driver.implicitly_wait(4)
        with allure.step("Найти элемент на странице и нажать на него"):
            login = driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        driver.implicitly_wait(4)

class LoginPage_5:
    def performance_glitch_user (self,driver,param:str):
        with allure.step("Найти элемент на странице"):
            user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
        with allure.step("Отправить значение логина"):
            user_name = driver.send_keys('standard_user')
        with allure.step("Найти элемент на странице"):
            password = driver.find_element(By.CSS_SELECTOR, '#password')
        with allure.step("Отправить значение пароля"):
            password = driver.send_keys('secret_sauce')
        driver.implicitly_wait(4)
        with allure.step("Найти элемент на странице и нажать на него"):
            login = driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        driver.implicitly_wait(4)