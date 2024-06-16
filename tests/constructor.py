from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import URL_MAIN
from locators import RegistrationData, LoginData, UI
import time


class TestConstructor:

    @staticmethod
    def test_constructor_switch_tabs_buns_sauces_fillings_click_on_tabs_transitions_succeeded():

        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(URL_MAIN)
        assert driver.current_url == URL_MAIN

        driver.find_element(*UI.GO_TO_SAUCES).click()   #  Т.к. по умолчанию открываются булки - переходим сначала в другой раздел, а оттуда - в buns, проверяя переход
        time.sleep(1)

        WebDriverWait(driver, 8).until(expected_conditions.element_to_be_clickable(UI.BUNS_SECTOR)).click()              # !
        time.sleep(1)
        WebDriverWait(driver, 8).until(expected_conditions.element_to_be_clickable(UI.SAUCES_SECTOR)).click()
        time.sleep(1)
        WebDriverWait(driver, 8).until(expected_conditions.element_to_be_clickable(UI.FILLINGS_SECTOR)).click()
        time.sleep(1)

        driver.find_element(*UI.SELECTED_SECTOR).click()
        assert driver.find_element(*UI.BUNS_SECTOR).text == 'Булки'
        assert driver.find_element(*UI.SAUCES_SECTOR).text == 'Соусы'
        assert driver.find_element(*UI.FILLINGS_SECTOR).text == 'Начинки'

        # не совсем понял, как проверить, что поменялся локатор. Например при переходе по табам "соусы", "булки" итд
