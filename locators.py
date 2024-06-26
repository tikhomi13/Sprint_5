from selenium.webdriver.common.by import By

class RegistrationData:                                                                                                    # РЕГИСТРАЦИЯ

    REGISTER_BUTTON = (By.XPATH, ".//button[contains(@class,'33qZ0') and (text()='Зарегистрироваться')]")         # Кнопка "Зарегистрироваться" в окне регистрации

    REGISTER_BUTTON_ON_LOGIN_SCREEN = (By.XPATH, ".//a[@href='/register' and (text()='Зарегистрироваться')]")              # Кнопка 'Зарегистрироваться' на экране логина

    NAME_FIELD = (By.XPATH, ".//label[contains(text(), 'Имя')]/following-sibling::input[@type='text']")                    # Поле "Имя"

    EMAIL_FIELD = (By.XPATH, ".//label[contains(text(), 'Email')]/following-sibling::input[@type='text']")                 # Поле 'Email'

    PASSWORD_FIELD = (By.XPATH, ".//fieldset[3]//input[@name='Пароль']")                                                   # Поле 'Пароль'

    INCORRECT_PASSWORD_TEXT = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")                                   # Текст ошибки неверного пароля

    SHOW_PASSWORD_WHILE_SIGNUP = (By.XPATH, ".//div[contains(@class, 'input__icon')]/*[1]")                                # Кнопка видимости пароля в форме регистрации




class LoginData:                                                                                                          # ВХОД (ЛОГИН)

    EMAIL_FIELD = (By.XPATH, ".//div/label[contains(text(), 'Email')]/following-sibling::input[@type='text']")            # Поле 'Email'

    PASSWORD_FIELD = (By.XPATH, ".//fieldset[2]//input[@name='Пароль']")                                                  # Поле 'Пароль'

    LOGIN_BUTTON_MAINPAGE = (By.XPATH, ".//button[(text()='Войти в аккаунт')]")                                           # Кнопка 'Войти в аккаунт' на главной

    LOG_IN_BUTTON_LK_SCREEN = (By.XPATH, ".//button[contains(@class, '1O7Bx') and (text()='Войти')][1]")                  # Кнопка 'Войти' после нажатия на 'Личный кабинет'

    LOGIN_BUTTON_RECOVER_REG = (By.XPATH, ".//a[@href='/login' and (text()='Войти')]")                                    # Кнопки 'Войти' в форме регистрации
                                                                                                                          # и в форме восстановления пароль
    RECOVER_BUTTON = (By.XPATH, ".//a[(text()='Восстановить пароль')]")                                                   # Кнопка 'Восстановить пароль'

    TEXT_ON_THE_AUTH_SCREEN = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2[(text()='Вход')]")                        # Текст 'Вход' экрана авторизации (вызывать методом text)

    ALREADY_REGISTERED = (By.XPATH, ".//p[1][(text()='Уже зарегистрированы?') and contains(@class, undefined)]")          # Текст 'Уже зарегистрированы?'
                                                                                                                          # Либо: ".//div//main//div/p/text()[1]"
                                                                                                                          # Для вывода самого текста - добавить .text


class UI:                                                                                                                 # ПОЛЬЗОВАТЕЛЬСКИЙ ИНТЕРФЕЙС

    LK_BUTTON_IN_HEADER = (By.XPATH, "//p[(text()='Личный Кабинет')]/ancestor::a[@href='/account']")                      # Кнопка 'Личный кабинет' в хедере

    GO_TO_CONSTRUCTOR_FROM_HEADER = (By.XPATH, ".//p[(text()='Конструктор')]/ancestor::a[@href='/']")                     # Кнопка перехода в 'Конструктор' в хедере

    GO_TO_CONSTRUCTOR_FROM_LOGO = (By.XPATH, "//*[local-name()='svg'][@fill='none']/ancestor::a[@href='/']")              # Переход в конструктор по клику на
                                                                                                                          # логотип Stellar Burgers в хедере
    EXIT_BUTTON = (By.XPATH, ".//button[(text()='Выход')]")                                                               # Кнопка 'Выйти из аккаунта' - расположена в ЛК

    BUNS_NOT_SELECTED_AND_CLICKABLE = (By.XPATH, ".//div[1]/span[(text()='Булки')]/ancestor::div[contains(@class, 'tab_tab__1SPyG')]")            # "Булки". Не выбрано (кликабельно)

    SAUCES_NOT_SELECTED_AND_CLICKABLE = (By.XPATH, ".//div[2]/span[(text()='Соусы')]/ancestor::div[contains(@class, 'tab_tab__1SPyG')]")          # Соусы. Не выбрано (кликабельно)

    FILLINGS_NOT_SELECTED_AND_CLICKABLE = (By.XPATH, ".//div[3]/span[(text()='Начинки')]/ancestor::div[contains(@class, 'tab_tab__1SPyG')]")      # Начинки. Не выбрано (кликабельно)

    BUNS_SELECTED = (By.XPATH, ".//div[1]/span[(text()='Булки')]/ancestor::div[contains(@*, 'pr-10') and contains(@class, 'type_current__2BEPc')]")           # Булки (выбрано)           #  "//div/main/section[1]/div[@style='display: flex;']"

    SAUCES_SELECTED = (By.XPATH, ".//div[2]/span[(text()='Соусы')]/ancestor::div[contains(@*, 'pr-10') and contains(@class, 'type_current__2BEPc')]")         # Соусы (выбрано)

    FILLINGS_SELECTED = (By.XPATH, ".//div[3]/span[(text()='Начинки')]/ancestor::div[contains(@*, 'pr-10') and contains(@class, 'type_current__2BEPc')]")     # Начинки (выбрано

    TABS_PANEL_SELECTED = (By.XPATH, "//section[1]/div[@style='display: flex;']")                                         # Панель табов

    STELLAR_BURGERS_LOGO_CSS = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")                                        # Логотип Stellar Burgers (CSS селектор)
                                                                                                                          # XPATH: .//div[@class='AppHeader_header__logo__2D0X2']
    PLACE_AN_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")                                              # Кнопка 'Оформить заказ'

    ASSEMBLE_THE_BURGER = (By.XPATH, ".//h1[(text()='Соберите бургер')]")                                                 #  Текст "Соберите бургер" в конструкторе
