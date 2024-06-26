from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import get_sign_up_data
from locators import RegistrationData, LoginData, UI


class TestRegistration:

    @staticmethod
    def test_signup_with_correct_data_successful_sign_up(driver, generator):

        name, email, password = generator
        driver.find_element(*UI.LK_BUTTON_IN_HEADER).click()
        driver.find_element(*RegistrationData.REGISTER_BUTTON_ON_LOGIN_SCREEN).click()
        driver.find_element(*RegistrationData.NAME_FIELD).send_keys(name)
        driver.find_element(*RegistrationData.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationData.PASSWORD_FIELD).send_keys(password)

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(RegistrationData.SHOW_PASSWORD_WHILE_SIGNUP))
        driver.find_element(*RegistrationData.SHOW_PASSWORD_WHILE_SIGNUP).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(RegistrationData.REGISTER_BUTTON))
        driver.find_element(*RegistrationData.REGISTER_BUTTON).click()
        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(LoginData.RECOVER_BUTTON))

        driver.find_element(*LoginData.EMAIL_FIELD).clear()
        driver.find_element(*LoginData.PASSWORD_FIELD).clear()
        driver.find_element(*LoginData.EMAIL_FIELD).send_keys(email)
        driver.find_element(*LoginData.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*LoginData.LOG_IN_BUTTON_LK_SCREEN).click()

        WebDriverWait(driver, 8).until(expected_conditions.visibility_of_element_located(UI.PLACE_AN_ORDER_BUTTON))
        assert driver.find_element(*UI.PLACE_AN_ORDER_BUTTON).is_displayed()

    @staticmethod
    def test_signup_with_incorrect_password_show_red_text(driver):

        name, email, password = get_sign_up_data()
        driver.find_element(*UI.LK_BUTTON_IN_HEADER).click()
        driver.find_element(*RegistrationData.REGISTER_BUTTON_ON_LOGIN_SCREEN).click()
        driver.find_element(*RegistrationData.NAME_FIELD).send_keys(name)
        driver.find_element(*RegistrationData.EMAIL_FIELD).send_keys(email)
        driver.find_element(*RegistrationData.PASSWORD_FIELD).send_keys('55555')
        driver.find_element(*RegistrationData.REGISTER_BUTTON).click()

        WebDriverWait(driver, 6).until(expected_conditions.text_to_be_present_in_element(RegistrationData.INCORRECT_PASSWORD_TEXT, 'Некорректный пароль'))
        assert driver.find_element(*RegistrationData.INCORRECT_PASSWORD_TEXT).is_displayed()
