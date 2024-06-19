from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import get_sign_up_data

from locators import RegistrationData, LoginData, UI


class TestRegistration:

    @staticmethod
    def test_signup_with_correct_data_successful_sign_up(generator, register):

        WebDriverWait(register, 8).until(expected_conditions.visibility_of_element_located(UI.PLACE_AN_ORDER_BUTTON))

        assert register.find_element(*UI.PLACE_AN_ORDER_BUTTON).text == 'Оформить заказ'

    @staticmethod
    def test_signup_with_incorrect_password_show_red_text(register):

        name, email, password = get_sign_up_data()

        register.find_element(*RegistrationData.NAME_FIELD).send_keys(name)
        register.find_element(*RegistrationData.EMAIL_FIELD).send_keys(email)
        register.find_element(*RegistrationData.PASSWORD_FIELD).send_keys('55555')  # Неверный пароль ( < 6 симв)

        register.find_element(*RegistrationData.REGISTER_BUTTON).click()  # Зарегистрироваться
        WebDriverWait(register, 5).until(expected_conditions.visibility_of_element_located(RegistrationData.INCORRECT_PASSWORD_TEXT))

        assert register.find_element(*RegistrationData.INCORRECT_PASSWORD_TEXT).text == 'Некорректный пароль'
