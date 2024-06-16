# Здесь хранятся фикстуры

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import URL_MAIN, MY_LOGIN, MY_PASSWORD
from locators import RegistrationData, LoginData, UI


def browser_settings():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    return chrome_options


@pytest.fixture
def driver():  # Фикстура для открытия сайта

    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get(URL_MAIN)

    WebDriverWait(chrome, 10).until(expected_conditions.visibility_of_element_located(UI.STELLAR_BURGERS_LOGO_CSS))
    assert chrome.current_url == URL_MAIN, "URL is wrong"

    yield chrome
    chrome.quit()


@pytest.fixture
def auth_lk():  # Фикстура для авторизации на сайте через клик по кнопке "Личный кабинет"

    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get(URL_MAIN)

    WebDriverWait(chrome, 10).until(expected_conditions.visibility_of_element_located(UI.STELLAR_BURGERS_LOGO_CSS))
    assert chrome.current_url == URL_MAIN, "URL is wrong"

    chrome.find_element(*UI.LK_BUTTON_IN_HEADER).click()
    assert 'login' in chrome.current_url

    chrome.find_element(*LoginData.EMAIL_FIELD).send_keys(MY_LOGIN)
    chrome.find_element(*LoginData.PASSWORD_FIELD).send_keys(MY_PASSWORD)

    chrome.find_element(*LoginData.LOG_IN_BUTTON_LK_SCREEN).click()
    WebDriverWait(chrome, 5).until(expected_conditions.element_to_be_clickable(UI.PLACE_AN_ORDER_BUTTON))

    yield chrome
    chrome.quit()


@pytest.fixture
def register():

    chrome = webdriver.Chrome(options=browser_settings())
    chrome.get(URL_MAIN)

    WebDriverWait(chrome, 10).until(expected_conditions.visibility_of_element_located(UI.STELLAR_BURGERS_LOGO_CSS))
    assert chrome.current_url == URL_MAIN, "URL is wrong"

    chrome.find_element(*UI.LK_BUTTON_IN_HEADER).click()
    chrome.find_element(*RegistrationData.REGISTER_BUTTON_ON_LOGIN_SCREEN).click()

    yield chrome
    chrome.quit()
