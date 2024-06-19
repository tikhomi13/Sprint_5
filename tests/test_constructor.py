from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import RegistrationData, LoginData, UI


class TestConstructor:

    @staticmethod
    def test_constructor_switch_tabs_buns_click_on_tabs_transitions_succeeded(driver):

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(UI.STELLAR_BURGERS_LOGO_CSS))
        driver.find_element(*UI.SAUCES_NOT_SELECTED_AND_CLICKABLE).click()

        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(UI.SAUCES_SELECTED))
        driver.find_element(*UI.BUNS_NOT_SELECTED_AND_CLICKABLE).click()                     # !

        WebDriverWait(driver, 8).until(expected_conditions.element_to_be_clickable(UI.BUNS_SELECTED))                        # !

        assert driver.find_element(*UI.BUNS_SELECTED).is_displayed()

    @staticmethod
    def test_constructor_switch_tabs_sauces_click_on_tabs_transitions_succeeded(driver):

        WebDriverWait(driver, 8).until(expected_conditions.element_to_be_clickable(UI.SAUCES_NOT_SELECTED_AND_CLICKABLE)).click()

        assert driver.find_element(*UI.SAUCES_SELECTED).is_displayed()

    @staticmethod
    def test_constructor_switch_tabs_fillings_click_on_tabs_transitions_succeeded(driver):

        driver.find_element(*UI.TABS_PANEL_SELECTED).click()
        WebDriverWait(driver, 8).until(expected_conditions.element_to_be_clickable(UI.FILLINGS_NOT_SELECTED_AND_CLICKABLE)).click()

        assert driver.find_element(*UI.FILLINGS_SELECTED).is_displayed()
