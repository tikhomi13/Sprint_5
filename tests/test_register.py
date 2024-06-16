from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import URL_MAIN
from locators import RegistrationData, LoginData, UI
from data import get_sign_up_data
import time


class TestRegistration:

    @staticmethod
    def test_signup_with_correct_data_successful_sign_up(register):

        name, email, password = get_sign_up_data()   #  Генерация данных

        register.find_element(*RegistrationData.NAME_FIELD).send_keys(name)
        register.find_element(*RegistrationData.EMAIL_FIELD).send_keys(email)
        register.find_element(*RegistrationData.PASSWORD_FIELD).send_keys(password)

        register.find_element(*RegistrationData.REGISTER_BUTTON).click()  #  Регистрация

        WebDriverWait(register, 8).until(expected_conditions.visibility_of_element_located(LoginData.RECOVER_BUTTON))
        register.find_element(*LoginData.EMAIL_FIELD).clear()
        register.find_element(*LoginData.PASSWORD_FIELD).clear()

        time.sleep(1)

        register.find_element(*LoginData.EMAIL_FIELD).send_keys(email)
        register.find_element(*LoginData.PASSWORD_FIELD).send_keys(password)
        register.find_element(*LoginData.LOG_IN_BUTTON_LK_SCREEN).click()  # Авторизация

        WebDriverWait(register, 8).until(expected_conditions.visibility_of_element_located(UI.PLACE_AN_ORDER_BUTTON))
        time.sleep(2)

        assert register.find_element(*UI.PLACE_AN_ORDER_BUTTON).text == 'Оформить заказ'


    @staticmethod
    def test_signup_with_incorrect_password_show_red_text(register):

        name, email, password = get_sign_up_data()

        register.find_element(*RegistrationData.NAME_FIELD).send_keys(name)
        register.find_element(*RegistrationData.EMAIL_FIELD).send_keys(email)
        register.find_element(*RegistrationData.PASSWORD_FIELD).send_keys('55555') # Некорректный пароль

        time.sleep(2)
        register.find_element(*RegistrationData.SHOW_PASSWORD_WHILE_SIGNUP).click()
        time.sleep(1)

        register.find_element(*RegistrationData.REGISTER_BUTTON).click()  #  Зарегистрироваться
        WebDriverWait(register, 5).until(expected_conditions.visibility_of_element_located(RegistrationData.INCORRECT_PASSWORD_TEXT))        # Или presence

        assert register.find_element(*RegistrationData.INCORRECT_PASSWORD_TEXT).text == 'Некорректный пароль'
