from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL_MAIN
from locators import RegistrationData, LoginData, UI


class TestGoToConstructor:

    @staticmethod
    def test_go_to_constructor_click_on_constructor_transition_succeeded(driver):

        driver.get(f'{URL_MAIN}login')  #  Перед переходом в конструктор уходим на экран логина, где нет конструктора, чтобы проверить, что конструктор именно появился
        WebDriverWait(driver, 12).until(expected_conditions.visibility_of_element_located(LoginData.TEXT_ON_THE_AUTH_SCREEN))

        driver.find_element(*UI.GO_TO_CONSTRUCTOR_FROM_HEADER).click()
        # Клик по кнопке "Конструктор"
        WebDriverWait(driver, 6).until(expected_conditions.text_to_be_present_in_element(UI.ASSEMBLE_THE_BURGER, 'Соберите бургер'))

        assert driver.find_element(*UI.ASSEMBLE_THE_BURGER).is_displayed()

    @staticmethod
    def test_go_to_constructor_click_on_main_logo_transition_succeeded(driver):

        driver.get(f'{URL_MAIN}login')
        WebDriverWait(driver, 12).until(expected_conditions.visibility_of_element_located(LoginData.TEXT_ON_THE_AUTH_SCREEN))

        driver.find_element(*UI.GO_TO_CONSTRUCTOR_FROM_LOGO).click()
        # Клик по лого Stellar Burgers
        WebDriverWait(driver, 6).until(expected_conditions.text_to_be_present_in_element(UI.ASSEMBLE_THE_BURGER, 'Соберите бургер'))

        assert driver.find_element(*UI.ASSEMBLE_THE_BURGER).is_displayed()
