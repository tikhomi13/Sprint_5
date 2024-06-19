# Здесь хранятся фикстуры

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import URL_MAIN, MY_LOGIN, MY_PASSWORD
from locators import RegistrationData, LoginData, UI
from data import get_sign_up_data        # Генератор данных для фикстуры generator (с паролем)


@pytest.fixture
def driver():  # Фикстура для открытия сайта (браузера)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')

    chrome = webdriver.Chrome(options=chrome_options)
    chrome.get(URL_MAIN)

    WebDriverWait(chrome, 10).until(expected_conditions.visibility_of_element_located(UI.STELLAR_BURGERS_LOGO_CSS))

    yield chrome
    chrome.quit()


@pytest.fixture
def auth_lk(driver):  # Фикстура для авторизации на сайте через клик по кнопке "Личный кабинет"

    driver.find_element(*UI.LK_BUTTON_IN_HEADER).click()
    driver.find_element(*LoginData.EMAIL_FIELD).send_keys(MY_LOGIN)

    driver.find_element(*LoginData.PASSWORD_FIELD).send_keys(MY_PASSWORD)
    # меняем chrome на driver т.к. у нас вложенная фикстура и нужен ее аргумент

    driver.find_element(*LoginData.LOG_IN_BUTTON_LK_SCREEN).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(UI.PLACE_AN_ORDER_BUTTON))

    yield driver
    driver.quit()


@pytest.fixture
def register(driver):  # Фикстура для открытия сайта и клика по кнопке "Регистрация" в разделе "Личный кабинет"

    driver.find_element(*UI.LK_BUTTON_IN_HEADER).click()
    driver.find_element(*RegistrationData.REGISTER_BUTTON_ON_LOGIN_SCREEN).click()

    yield driver
    driver.quit()


@pytest.fixture
def generator(register):   # Фикстура для генерации данных (и авторизации - разделить функционал не смог)

    name, email, password = get_sign_up_data()

    register.find_element(*RegistrationData.NAME_FIELD).send_keys(name)
    register.find_element(*RegistrationData.EMAIL_FIELD).send_keys(email)
    register.find_element(*RegistrationData.PASSWORD_FIELD).send_keys(password)

    WebDriverWait(register, 5).until(expected_conditions.element_to_be_clickable(RegistrationData.SHOW_PASSWORD_WHILE_SIGNUP))
    register.find_element(*RegistrationData.SHOW_PASSWORD_WHILE_SIGNUP).click()

    WebDriverWait(register, 5).until(expected_conditions.element_to_be_clickable(RegistrationData.REGISTER_BUTTON))
    register.find_element(*RegistrationData.REGISTER_BUTTON).click()  # Регистрация

    WebDriverWait(register, 8).until(expected_conditions.visibility_of_element_located(LoginData.RECOVER_BUTTON))
    register.find_element(*LoginData.EMAIL_FIELD).clear()
    register.find_element(*LoginData.PASSWORD_FIELD).clear()

    register.find_element(*LoginData.EMAIL_FIELD).send_keys(email)
    register.find_element(*LoginData.PASSWORD_FIELD).send_keys(password)
    register.find_element(*LoginData.LOG_IN_BUTTON_LK_SCREEN).click()  # Авторизация
