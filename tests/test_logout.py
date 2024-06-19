from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import RegistrationData, LoginData, UI


class TestLogOut:

    @staticmethod
    def test_logout_after_successful_login_logout_completed(auth_lk):

        WebDriverWait(auth_lk, 5).until(expected_conditions.text_to_be_present_in_element(UI.PLACE_AN_ORDER_BUTTON, 'Оформить заказ'))
        auth_lk.find_element(*UI.LK_BUTTON_IN_HEADER).click()

        WebDriverWait(auth_lk, 5).until(expected_conditions.element_to_be_clickable(UI.EXIT_BUTTON))
        auth_lk.find_element(*UI.EXIT_BUTTON).click()

        WebDriverWait(auth_lk, 6).until(expected_conditions.element_to_be_clickable(RegistrationData.REGISTER_BUTTON_ON_LOGIN_SCREEN))
        assert auth_lk.find_element(*RegistrationData.REGISTER_BUTTON_ON_LOGIN_SCREEN).text == 'Зарегистрироваться'
