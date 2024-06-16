from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import URL_MAIN, MY_LOGIN, MY_PASSWORD
from locators import RegistrationData, LoginData, UI
import time


class TestLogin:

    @staticmethod
    def test_try_to_login_from_main_page_success_login(driver):

        driver.find_element(*LoginData.LOGIN_BUTTON_MAINPAGE).click()

        assert 'login' in driver.current_url

        driver.find_element(*LoginData.EMAIL_FIELD).send_keys(MY_LOGIN)
        driver.find_element(*LoginData.PASSWORD_FIELD).send_keys(MY_PASSWORD)

        driver.find_element(*LoginData.LOG_IN_BUTTON_LK_SCREEN).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(UI.PLACE_AN_ORDER_BUTTON))

        assert driver.find_element(*UI.PLACE_AN_ORDER_BUTTON).text == 'Оформить заказ'

    @staticmethod
    def test_try_to_login_from_lk_success_login(auth_lk):

        assert auth_lk.find_element(*UI.PLACE_AN_ORDER_BUTTON).text == 'Оформить заказ'

    @staticmethod
    def test_try_to_login_from_registration_form_success_login(driver):

        driver.find_element(*UI.LK_BUTTON_IN_HEADER).click()
        driver.find_element(*RegistrationData.REGISTER_BUTTON_ON_LOGIN_SCREEN).click()

        time.sleep(1)
        element_to_scroll = driver.find_element(*LoginData.ALREADY_REGISTERED)
        driver.execute_script("arguments[0]. scrollIntoView();", element_to_scroll)

        time.sleep(2)
        assert element_to_scroll.text == 'Уже зарегистрированы? Войти'  # проверка загрузки страницы регистрации
        driver.find_element(*LoginData.LOGIN_BUTTON_RECOVER_REG).click()

        driver.find_element(*LoginData.EMAIL_FIELD).send_keys(MY_LOGIN)
        driver.find_element(*LoginData.PASSWORD_FIELD).send_keys(MY_PASSWORD)
        time.sleep(1)

        driver.find_element(*LoginData.LOG_IN_BUTTON_LK_SCREEN).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(UI.PLACE_AN_ORDER_BUTTON))

        assert driver.find_element(*UI.PLACE_AN_ORDER_BUTTON).text == 'Оформить заказ'

    @staticmethod
    def test_try_to_login_from_password_recovery_page_success_login(driver):

        driver.find_element(*UI.LK_BUTTON_IN_HEADER).click()

        driver.find_element(*LoginData.RECOVER_BUTTON).click()

        driver.find_element(*LoginData.LOGIN_BUTTON_RECOVER_REG).click()

        assert 'login' in driver.current_url

        driver.find_element(*LoginData.EMAIL_FIELD).send_keys(MY_LOGIN)
        driver.find_element(*LoginData.PASSWORD_FIELD).send_keys(MY_PASSWORD)

        driver.find_element(*LoginData.LOG_IN_BUTTON_LK_SCREEN).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(UI.PLACE_AN_ORDER_BUTTON))

        assert driver.find_element(*UI.PLACE_AN_ORDER_BUTTON).text == 'Оформить заказ'
