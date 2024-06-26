import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL_MAIN, MY_LOGIN, MY_PASSWORD
from locators import RegistrationData, LoginData, UI
from data import get_sign_up_data


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
def auth_lk(driver):  # Фикстура авторизации

    driver.find_element(*UI.LK_BUTTON_IN_HEADER).click()
    driver.find_element(*LoginData.EMAIL_FIELD).send_keys(MY_LOGIN)
    driver.find_element(*LoginData.PASSWORD_FIELD).send_keys(MY_PASSWORD)
    driver.find_element(*LoginData.LOG_IN_BUTTON_LK_SCREEN).click()
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(UI.PLACE_AN_ORDER_BUTTON))
    yield driver


@pytest.fixture
def generator(driver):   # Фикстура генерации данных
    name, email, password = get_sign_up_data()
    return name, email, password
