# Здесь находятся локаторы для тестирования Stellar Burgers и их описание

from selenium.webdriver.common.by import By


class RegistrationData:                                                                                                    # РЕГИСТРАЦИЯ

    #REGISTER_BUTTON = (By.XPATH, ".//div/form/button[contains(@class,'33qZ0')]")                                          # Кнопка "Зарегистрироваться" в окне регистрации

    REGISTER_BUTTON = (By.XPATH, ".//div/form/button[contains(@class,'33qZ0') and (text()='Зарегистрироваться')]")         # Исправлено

    # REGISTER_BUTTON_ON_LOGIN_SCREEN = (By.XPATH, ".//a[@href='/register']")                                               # Кнопка 'Зарегистрироваться' на экране логина

    REGISTER_BUTTON_ON_LOGIN_SCREEN = (By.XPATH, ".//a[@href='/register' and (text()='Зарегистрироваться')]")  # Исправлено

    # NAME_FIELD = (By.XPATH, ".//fieldset[1]/div/div/input[@class='text input__textfield text_type_main-default']")        # Поле "Имя"

    NAME_FIELD = (By.XPATH, ".//fieldset[1]/div/div/label[contains(text(), 'Имя')]/following-sibling::input[@type='text']") # Исправлено - применен following-siblings

    # EMAIL_FIELD = (By.XPATH, ".//fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default']")       # Поле 'Email'

    EMAIL_FIELD = (By.XPATH, ".//div/form/fieldset[2]/div/div/label[contains(text(), 'Email')]/following-sibling::input[@type='text']")  # Исправлено

    # PASSWORD_FIELD = (By.XPATH, ".//fieldset[3]/div/div/input[@class='text input__textfield text_type_main-default']")    # Поле 'Пароль'

    PASSWORD_FIELD = (By.XPATH, ".//fieldset[3]/div/div/input[@class='text input__textfield text_type_main-default' and @name='Пароль']")    #  Исправлено

    # INCORRECT_PASSWORD_TEXT = (By.CSS_SELECTOR, ".input__error")                                                          # Текст ошибки неверного пароля

    INCORRECT_PASSWORD_TEXT = (By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[3]/div/p[contains(@class, 'input') and contains(text(), 'Некорректный пароль')]")  #  Исправлено

    #SHOW_PASSWORD_WHILE_SIGNUP = (By.XPATH, ".//div/div/div[contains(@class, 'input__icon')]/*[1]")                        # Кнопка видимости пароля в форме регистрации

    SHOW_PASSWORD_WHILE_SIGNUP = (By.XPATH, ".//*[@id='root']//div/div[contains(@class, 'input__icon')]/*[1]")              #  Исправлено




class LoginData:                                                                                                          # ВХОД (ЛОГИН)

    # EMAIL_FIELD = (By.XPATH, ".//fieldset[1]/div/div/input[@class='text input__textfield text_type_main-default']")     # Поле 'Email'

    EMAIL_FIELD = (By.XPATH, ".//div/form/fieldset[1]/div/div/label[contains(text(), 'Email')]/following-sibling::input[@type='text']")       # Исправлено

    # PASSWORD_FIELD = (By.XPATH, ".//fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default']")  # Поле 'Пароль'

    PASSWORD_FIELD = (By.XPATH, ".//fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default' and @name='Пароль']")     # Исправлено

    #LOGIN_BUTTON_MAINPAGE = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")                                 # Кнопка 'Войти в аккаунт' на главной

    LOGIN_BUTTON_MAINPAGE = (By.XPATH, ".//button[(text()='Войти в аккаунт')][1]")                                        # Исправлено

    #LOG_IN_BUTTON_LK_SCREEN = (By.XPATH, ".//button[contains(text(), 'Войти')][1]")                                      # Кнопка 'Войти' после нажатия на 'Личный кабинет'

    LOG_IN_BUTTON_LK_SCREEN = (By.XPATH, ".//button[contains(@class, '1O7Bx') and (text()='Войти')][1]")                  # Исправлено

    # LOGIN_BUTTON_RECOVER_REG = (By.XPATH, ".//a[@href='/login']")                                                       # Кнопки 'Войти' в форме регистрации
                                                                                                                          # и в форме восстановления пароля
    LOGIN_BUTTON_RECOVER_REG = (By.XPATH, ".//a[@href='/login' and (text()='Войти')]")                                    # Исправлено

    # RECOVER_BUTTON = (By.XPATH, ".//a[@href='/forgot-password']")                                                       # Кнопка 'Восстановить пароль'

    RECOVER_BUTTON = (By.XPATH, ".//a[@href='/forgot-password' and (text()='Восстановить пароль')]")                      # Исправлено

    # TEXT_ON_THE_AUTH_SCREEN = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2")                                       # Текст 'Вход' экрана авторизации (вызывать методом text)

    TEXT_ON_THE_AUTH_SCREEN = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2[(text()='Вход')]")                        # Исправлено

    # ALREADY_REGISTERED = (By.XPATH, ".//p[1][contains(text(), 'Уже')]")                                                 # Текст 'Уже зарегистрированы?'
                                                                                                                          # Либо: ".//div//main//div/p/text()[1]"
                                                                                                                          # Для вывода самого текста - добавить .text
    ALREADY_REGISTERED = (By.XPATH, ".//p[1][(text()='Уже зарегистрированы?') and contains(@class, undefined)]")          # Исправлено



class UI:                                                                                                                 # ПОЛЬЗОВАТЕЛЬСКИЙ ИНТЕРФЕЙС

    # LK_BUTTON_IN_HEADER = (By.XPATH, ".//a[@href='/account']")                                                          # Кнопка 'Личный кабинет' в хедере

    LK_BUTTON_IN_HEADER = (By.XPATH, "//*[@id='root']/div/header[contains(@class, 'X9')]/nav/a/p[(text()='Личный Кабинет')]/ancestor::a[@href='/account']") # Исправлено
                                                                                                                                                            # Применен ancestor
    # GO_TO_CONSTRUCTOR_FROM_HEADER = (By.XPATH, ".//li/a[@href='/']")                                                    # Кнопка перехода в 'Конструктор' в хедере

    GO_TO_CONSTRUCTOR_FROM_HEADER = (By.XPATH, ".//li/a/p[(text()='Конструктор')]/ancestor::a[@href='/']")                # Исправлено

    # GO_TO_CONSTRUCTOR_FROM_LOGO = (By.XPATH, ".//div/a[@href='/']")                                                     # Переход в конструктор по клику на
                                                                                                                          # логотип Stellar Burgers в хедере
    GO_TO_CONSTRUCTOR_FROM_LOGO = (By.XPATH, "//*[local-name()='svg'][@fill='none']/ancestor::a[@href='/']")              # Исправлено

    # EXIT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Выход')]")                                                    # Кнопка 'Выйти из аккаунта' - расположена в ЛК

    EXIT_BUTTON = (By.XPATH, ".//li/button[contains(@class, '14Yp3') and (text()='Выход')]")                              # Исправлено

    BUNS_NOT_SELECTED_AND_CLICKABLE = (By.XPATH, ".//div[1]/span[(text()='Булки')]/ancestor::div[contains(@class, 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect')]")            # "Булки". Не выбрано (кликабельно)

    SAUCES_NOT_SELECTED_AND_CLICKABLE = (By.XPATH, ".//div[2]/span[(text()='Соусы')]/ancestor::div[contains(@class, 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect')]")          # Соусы. Не выбрано (кликабельно)

    FILLINGS_NOT_SELECTED_AND_CLICKABLE = (By.XPATH, ".//div[3]/span[(text()='Начинки')]/ancestor::div[contains(@class, 'tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect')]")      # Начинки. Не выбрано (кликабельно)

    BUNS_SELECTED = (By.XPATH, ".//div[1]/span[(text()='Булки')]/ancestor::div[contains(@*, 'pr-10') and contains(@class, 'type_current__2BEPc')]")           # Булки (выбрано)           #  "//div/main/section[1]/div[@style='display: flex;']"

    SAUCES_SELECTED = (By.XPATH, ".//div[2]/span[(text()='Соусы')]/ancestor::div[contains(@*, 'pr-10') and contains(@class, 'type_current__2BEPc')]")         # Соусы (выбрано)

    FILLINGS_SELECTED = (By.XPATH, ".//div[3]/span[(text()='Начинки')]/ancestor::div[contains(@*, 'pr-10') and contains(@class, 'type_current__2BEPc')]")     # Начинки (выбрано

    TABS_PANEL_SELECTED = (By.XPATH, "//div/main/section[1]/div[@style='display: flex;']")                                    # Панель табов

    STELLAR_BURGERS_LOGO_CSS = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")                                        # Логотип Stellar Burgers (CSS селектор)
                                                                                                                          # XPATH: .//div[@class='AppHeader_header__logo__2D0X2']
    # PLACE_AN_ORDER_BUTTON = (By.XPATH, ".//button[contains(text(), 'Оформить')]")                                       # Кнопка 'Оформить заказ'

    PLACE_AN_ORDER_BUTTON = (By.XPATH, ".//button[contains(@class, '33qZ0') and text()='Оформить заказ']")                # Исправлено

    # ASSEMBLE_THE_BURGER = (By.XPATH, ".//section/h1[contains(text(), 'Соберите бургер')]")                              #  Текст "Соберите бургер" в конструкторе

    ASSEMBLE_THE_BURGER = (By.XPATH, ".//section/h1[contains(@class, 'mb-5 mt-10') and (text()='Соберите бургер')]")      # Исправлено
