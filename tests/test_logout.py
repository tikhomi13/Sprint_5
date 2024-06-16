from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import URL_MAIN
from locators import RegistrationData, LoginData, UI
import time


class TestLogOut:

    @staticmethod
    def test_logout_after_successful_login_logout_completed(auth_lk):

        assert auth_lk.find_element(*UI.PLACE_AN_ORDER_BUTTON).text == 'Оформить заказ'
        assert auth_lk.current_url == URL_MAIN, "URL is wrong"

        auth_lk.find_element(*UI.LK_BUTTON_IN_HEADER).click()
        time.sleep(1)
        auth_lk.find_element(*UI.EXIT_BUTTON).click()
        time.sleep(2)

        WebDriverWait(auth_lk, 6).until(expected_conditions.element_to_be_clickable(RegistrationData.REGISTER_BUTTON_ON_LOGIN_SCREEN))
        assert auth_lk.find_element(*RegistrationData.REGISTER_BUTTON_ON_LOGIN_SCREEN).text == 'Зарегистрироваться'
