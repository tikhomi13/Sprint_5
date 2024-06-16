from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import URL_MAIN
from locators import RegistrationData, LoginData, UI
import time


class TestGoToConstructor:

    @staticmethod
    def test_go_to_constructor_click_on_constructor_transition_succeeded():

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(f'{URL_MAIN}login')  #  Перед переходом в конструктор уходим на экран логина, где нет конструктора, чтобы проверить, что конструктор именно появился
        WebDriverWait(driver, 12).until(expected_conditions.visibility_of_element_located(LoginData.TEXT_ON_THE_AUTH_SCREEN))

        time.sleep(1)
        assert driver.current_url == f'{URL_MAIN}login', "URL is wrong"
        driver.find_element(*UI.GO_TO_CONSTRUCTOR_FROM_HEADER).click()   # Клин по кнопке "Конструктор"

        time.sleep(1)
        WebDriverWait(driver, 6).until((expected_conditions.visibility_of_element_located(UI.ASSEMBLE_THE_BURGER)))
        assert driver.find_element(*UI.ASSEMBLE_THE_BURGER).text == 'Соберите бургер'

        driver.quit()

    @staticmethod
    def test_go_to_constructor_click_on_main_logo_transition_succeeded():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(f'{URL_MAIN}login')
        WebDriverWait(driver, 12).until(expected_conditions.visibility_of_element_located(LoginData.TEXT_ON_THE_AUTH_SCREEN))

        time.sleep(1)
        assert driver.current_url == f'{URL_MAIN}login', "URL is wrong"
        driver.find_element(*UI.GO_TO_CONSTRUCTOR_FROM_LOGO).click()      #  Клик по лого Stellar Burgers

        time.sleep(1)
        WebDriverWait(driver, 6).until((expected_conditions.visibility_of_element_located(UI.ASSEMBLE_THE_BURGER)))
        assert driver.find_element(*UI.ASSEMBLE_THE_BURGER).text == 'Соберите бургер'

        driver.quit()
