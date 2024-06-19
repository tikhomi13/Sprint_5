from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import UI


class TestGoToPersonalAccount:

    @staticmethod
    def test_go_to_lk_after_sign_in_lk_successfully_opened(auth_lk):

        auth_lk.find_element(*UI.LK_BUTTON_IN_HEADER).click()
        WebDriverWait(auth_lk, 8).until(expected_conditions.element_to_be_clickable(UI.EXIT_BUTTON))

        assert auth_lk.find_element(*UI.EXIT_BUTTON).text == 'Выход'
