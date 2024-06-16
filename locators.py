# Здесь находятся локаторы для тестирования Stellar Burgers и их описание

from selenium.webdriver.common.by import By


class RegistrationData:                                                                                                   # РЕГИСТРАЦИЯ

    REGISTER_BUTTON = (By.XPATH, ".//div/form/button[contains(@class,'33qZ0')]")                                          # Кнопка "Зарегистрироваться" в окне регистрации

    REGISTER_BUTTON_ON_LOGIN_SCREEN = (By.XPATH, ".//a[@href='/register']")                                               # Кнопка 'Зарегистрироваться' на экране логина

    NAME_FIELD = (By.XPATH, ".//fieldset[1]/div/div/input[@class='text input__textfield text_type_main-default']")        # Поле "Имя"

    EMAIL_FIELD = (By.XPATH, ".//fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default']")       # Поле 'Email'

    PASSWORD_FIELD = (By.XPATH, ".//fieldset[3]/div/div/input[@class='text input__textfield text_type_main-default']")    # Поле 'Пароль'

    INCORRECT_PASSWORD_TEXT = (By.CSS_SELECTOR, ".input__error")                                                          # Текст ошибки неверного пароля

    SHOW_PASSWORD_WHILE_SIGNUP = (By.XPATH, ".//div/div/div[contains(@class, 'input__icon')]/*[1]")                       # Кнопка видимости пароля в форме регистрации



class LoginData:                                                                                                          # ВХОД (ЛОГИН)

    EMAIL_FIELD = (By.XPATH, ".//fieldset[1]/div/div/input[@class='text input__textfield text_type_main-default']")       # Поле 'Email'

    PASSWORD_FIELD = (By.XPATH, ".//fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default']")    # Поле 'Пароль'

    LOGIN_BUTTON_MAINPAGE = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")                                  # Кнопка 'Войти в аккаунт' на главной

    LOG_IN_BUTTON_LK_SCREEN = (By.XPATH, ".//button[contains(text(), 'Войти')][1]")                                       # Кнопка 'Войти' после нажатия на 'Личный кабинет'

    LOGIN_BUTTON_RECOVER_REG = (By.XPATH, ".//a[@href='/login']")                                                         # Кнопки 'Войти' в форме регистрации
                                                                                                                          # и в форме восстановления пароля
    RECOVER_BUTTON = (By.XPATH, ".//a[@href='/forgot-password']")                                                         # Кнопка 'Восстановить пароль'

    TEXT_ON_THE_AUTH_SCREEN = (By.XPATH, ".//div[@class='Auth_login__3hAey']/h2")                                              # Текст 'Вход' экрана авторизации (вызывать методом text)

    ALREADY_REGISTERED = (By.XPATH, ".//p[1][contains(text(), 'Уже')]")                                                   # Текст 'Уже зарегистрированы?'
                                                                                                                          # Либо: ".//div//main//div/p/text()[1]"
                                                                                                                          # Для вывода самого текста - добавить .text


class UI:                                                                                                                 # ПОЛЬЗОВАТЕЛЬСКИЙ ИНТЕРФЕЙС

    LK_BUTTON_IN_HEADER = (By.XPATH, ".//a[@href='/account']")                                                            # Кнопка 'Личный кабинет' в хедере
                                                                                                                          # Текст на кнопке:  .//p[contains(text(), 'Личный')]
    GO_TO_CONSTRUCTOR_FROM_HEADER = (By.XPATH, ".//li/a[@href='/']")                                                      # Кнопка перехода в 'Конструктор' в хедере

    GO_TO_CONSTRUCTOR_FROM_LOGO = (By.XPATH, ".//div/a[@href='/']")                                                       # Переход в конструктор по клику на
                                                                                                                          # логотип Stellar Burgers в хедере
    EXIT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Выход')]")                                                      # Кнопка 'Выйти из аккаунта' - расположена в ЛК

    GO_TO_BUNS = (By.XPATH, ".//div[contains(@*, 'pr-10')][1]")                                                           # Переход к разделу 'Булки' <-- ! собака как символ синтаксиса

    GO_TO_SAUCES = (By.XPATH, ".//div[contains(@*, 'pr-10')][2]")                                                         # Переход к разделу 'Соусы' (раздел "Конструктор")

    GO_TO_FILLINGS = (By.XPATH, ".//div[contains(@*, 'pr-10')][3]")                                                       # Переход к разделу 'Начинки'

    BUNS_SECTOR = (By.XPATH, "//main/section[1]/div[1]/div[1]")                                                           # Раздел "Булки" "//div/main/section[1]/div[@style='display: flex;']"

    SAUCES_SECTOR = (By.XPATH, "//main/section[1]/div[1]/div[2]")                                                         # Раздел "Соусы"

    FILLINGS_SECTOR = (By.XPATH, "//main/section[1]/div[1]/div[3]")                                                       # Раздел "Начинки"

    BUNS_SECTOR_TEXT = (By.XPATH, "//main/section[1]/div[1]/div[1]/span")                                                 # Текст "Булки"

    SELECTED_SECTOR = (By.XPATH, "//div/main/section[1]/div[@style='display: flex;']")                                    # Выбранный раздел (панель табов)

    STELLAR_BURGERS_LOGO_CSS = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")                                        # Логотип Stellar Burgers (CSS селектор)
                                                                                                                          # XPATH: .//div[@class='AppHeader_header__logo__2D0X2']
    PLACE_AN_ORDER_BUTTON = (By.XPATH, ".//button[contains(text(), 'Оформить')]")                                         # Кнопка 'Оформить заказ'

    ASSEMBLE_THE_BURGER = (By.XPATH, ".//section/h1[contains(text(), 'Соберите бургер')]")                                #  Текст "Соберите бургер" в конструкторе
