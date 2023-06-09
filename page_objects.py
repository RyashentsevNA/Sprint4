from BaseApp import BasePage
from selenium.webdriver.common.by import By

class FireFoxLocators:
    LOCATOR_COOKIE_BUTTON = (By.ID, "rcc-confirm-button")  # Кнопка Cookie
    LOCATOR_FIRST_QUESTION_BUTTON = (By.ID, "accordion__heading-0")
    LOCATOR_SECOND_QUESTION_BUTTON = (By.ID, "accordion__heading-1")
    LOCATOR_THIRD_QUESTION_BUTTON = (By.ID, "accordion__heading-2")
    LOCATOR_FOURTH_QUESTION_BUTTON = (By.ID, "accordion__heading-3")
    LOCATOR_FIFTH_QUESTION_BUTTON = (By.ID, "accordion__heading-4")
    LOCATOR_SIXTH_QUESTION_BUTTON = (By.ID, "accordion__heading-5")
    LOCATOR_SEVENTH_QUESTION_BUTTON = (By.ID, "accordion__heading-6")
    LOCATOR_EIGHTH_QUESTION_BUTTON = (By.ID, "accordion__heading-7")
    LOCATOR_TOP_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")  # Кнопка заказа(верхняя)
    LOCATOR_DOWN_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")  # Кнопка заказа(нижняя)
    LOCATOR_NAME_FORM = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Form__17u6u div."
                                          "Input_InputContainer__3NykH:nth-child(1) > input.Input_Input__1iN_Z."
                                          "Input_Responsible__1jDKN")  # Поле для ввода имени
    LOCATOR_LASTNAME_FORM = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Form__17u6u"
                                              " div.Input_InputContainer__3NykH:nth-child(2) > "
                                              "input.Input_Input__1iN_Z.Input_Responsible__1jDKN")  # Поле для ввода фамилии
    LOCATOR_ADDRESS_FORM = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Form__17u6u "
                                             "div.Input_InputContainer__3NykH:nth-child(3) > "
                                             "input.Input_Input__1iN_Z.Input_Responsible__1jDKN")  # Поле для ввода адреса
    LOCATOR_METRO_FORM_BUTTON = (By.CLASS_NAME, "select-search__input")  # Кнопка указания метро
    LOCATOR_METRO_SQUARE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[3]/button")  # Выбор метро
    LOCATOR_PHONE_FORM = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Form__17u6u "
                                           "div.Input_InputContainer__3NykH:nth-child(5) > "
                                           "input.Input_Input__1iN_Z.Input_Responsible__1jDKN")  # Кнопка для ввода номера телефона
    LOCATOR_CONTINUE_BUTTON = (By.CSS_SELECTOR, "div:nth-child(2) div.App_App__15LM- div.Order_Content__bmtHS "
                                                "div.Order_NextButton__1_rCA > "
                                                "button.Button_Button__ra12g.Button_Middle__1CSJM")  # Кнопка продолжить(форма заказа)
    LOCATOR_DATE_BRING_SCOOTER = (By.XPATH, "//div[@class='react-datepicker__input-container']//input[@type='text']")  # Поле для ввода даты
    LOCATOR_DATE_BRING_SCOOTER_BUTTON = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS "
                                                          "div.Order_Form__17u6u div.Order_MixedDatePicker__3qiay "
                                                          "div.react-datepicker__tab-loop div.react-datepicker-popper "
                                                          "div.react-datepicker "
                                                          "div.react-datepicker__month-container:nth-child(4) "
                                                          "div.react-datepicker__month "
                                                          "div.react-datepicker__week:nth-child(3) > "
                                                          "div.react-datepicker__day.react-datepicker__day--018.react"
                                                          "-datepicker__day--weekend:nth-child(7)")# Подтверждение# даты в datepicker
    LOCATOR_RENTAL_PERIOD_BUTTON = (By.XPATH, "//div[@class='Dropdown-control']")  # Кнопка выбора периода времени катания
    LOCATOR_RENTAL_PERIOD_CHOICE = (By.CSS_SELECTOR, "div.Dropdown-option:nth-child(1)")  # Выбираем период времени
    LOCATOR_COLOR_SCOOTER = (By.CLASS_NAME, "Checkbox_Input__14A2w")  # Выбираем цвет самоката
    LOCATOR_COMMENTARY = (By.XPATH, "//div[@class='Order_Form__17u6u']//div[""@class='Input_InputContainer__3NykH']//input[@type='text']")# Поле для ввода комментария
    LOCATOR_ORDER_BUTTON = (By.CSS_SELECTOR, "div:nth-child(2) div.App_App__15LM- div.Order_Content__bmtHS "
                                             "div.Order_Buttons__1xGrp > "
                                             "button.Button_Button__ra12g.Button_Middle__1CSJM:nth-child(2)")  # Кнопка заказать в форме "заказа"
    LOCATOR_CONFIRM_BUTTON = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Modal__YZ-d3 "
                                               "div.Order_Buttons__1xGrp > "
                                               "button.Button_Button__ra12g.Button_Middle__1CSJM:nth-child(2)")  # Кнопка подтверждения заказа
    LOCATOR_CHECK_STATUS = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Modal__YZ-d3 "
                                             "div.Order_NextButton__1_rCA > "
                                             "button.Button_Button__ra12g.Button_Middle__1CSJM") # Кнопка проверить статус
    LOCATOR_YANDEX_BUTTON = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")  # Кнопка "Яндекс"
    LOCATOR_SCOOTER_BUTTON = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")  # Кнопка "Самокаты"
    LOCATOR_SHOW_STATUS = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS "
                                            "div.Order_Modal__YZ-d3 div.Order_NextButton__1_rCA > "
                                            "button.Button_Button__ra12g.Button_Middle__1CSJM")
    LOCATOR_UP_BOTTOM = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS "
                                          "div.Order_Modal__YZ-d3 div.Order_NextButton__1_rCA > "
                                          "button.Button_Button__ra12g.Button_Middle__1CSJM")

    LOCATOR_ABOUT_ARENDA = (By.CLASS_NAME, "Order_Header__BZXOb")
    LOCATOR_DOWN_BUTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")
    LOCATOR_TEXT_ARENDA = (By.CLASS_NAME, "Order_Header__BZXOb")



class Question_Program(BasePage):
    def do_first_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_COOKIE_BUTTON).click()
        self.driverwait(FireFoxLocators.LOCATOR_FIRST_QUESTION_BUTTON).click()

    def do_second_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_SECOND_QUESTION_BUTTON).click()

    def do_third_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_THIRD_QUESTION_BUTTON).click()

    def do_fourth_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_FOURTH_QUESTION_BUTTON).click()

    def do_fifth_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_FIFTH_QUESTION_BUTTON).click()

    def do_sixth_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_SIXTH_QUESTION_BUTTON).click()

    def do_seventh_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_SEVENTH_QUESTION_BUTTON).click()

    def do_eighth_question(self):
        self.driverwait(FireFoxLocators.LOCATOR_EIGHTH_QUESTION_BUTTON).click()


class Main_Page(BasePage):
    def click_to_order_top(self):
        self.driverwait(FireFoxLocators.LOCATOR_TOP_ORDER_BUTTON).click()

    def click_to_order_down(self):
        self.driverwait(FireFoxLocators.LOCATOR_DOWN_ORDER_BUTTON).click()

    def search_down_bottom(self):
        self.driverwait(FireFoxLocators.LOCATOR_DOWN_BUTTOM)


class Form_Order(BasePage):
    def fill_name(self):
        self.driverwait(FireFoxLocators.LOCATOR_NAME_FORM).send_keys('Вася')
        self.driverwait(FireFoxLocators.LOCATOR_LASTNAME_FORM).send_keys('Пупкин')

    # заполнить адрес и метро.
    def fill_address(self):
        self.driverwait(FireFoxLocators.LOCATOR_ADDRESS_FORM).send_keys('Улица Тестовая, дом 777')
        self.driverwait(FireFoxLocators.LOCATOR_METRO_FORM_BUTTON).click()
        self.driverwait(FireFoxLocators.LOCATOR_METRO_SQUARE_BUTTON).click()

    def fill_phone(self):
        self.driverwait(FireFoxLocators.LOCATOR_PHONE_FORM).send_keys('88005353535')
        self.driverwait(FireFoxLocators.LOCATOR_CONTINUE_BUTTON).click()

    def text_arenda(self):
        arenda = self.driverwait(FireFoxLocators.LOCATOR_TEXT_ARENDA)
        return arenda.text

class About_Rent(BasePage):
    # заполнить дату.
    def fill_date(self):
        self.driverwait(FireFoxLocators.LOCATOR_DATE_BRING_SCOOTER).send_keys('18.09.2022')
        self.driverwait(FireFoxLocators.LOCATOR_DATE_BRING_SCOOTER_BUTTON).click()
        self.driverwait(FireFoxLocators.LOCATOR_RENTAL_PERIOD_BUTTON).click()
        self.driverwait(FireFoxLocators.LOCATOR_RENTAL_PERIOD_CHOICE).click()

    # заполнить цвет, комментарий, нажать кнопку заказать, подтвердить заказ.
    def fill_other(self):
        self.driverwait(FireFoxLocators.LOCATOR_COLOR_SCOOTER).click()
        self.driverwait(FireFoxLocators.LOCATOR_COMMENTARY).send_keys('Привести к 11:00.')
        self.driverwait(FireFoxLocators.LOCATOR_ORDER_BUTTON).click()
        self.driverwait(FireFoxLocators.LOCATOR_CONFIRM_BUTTON).click()

    # нажать "проверить статус".
    def check_status(self):
        self.driverwait(FireFoxLocators.LOCATOR_CHECK_STATUS).click()

    def find_arenda_button(self):
        arenda_text = self.driverwait(FireFoxLocators.LOCATOR_CHECK_STATUS)
        return arenda_text.text

    def check_up_buttom(self):
        up_buttom = self.driverwait(FireFoxLocators.LOCATOR_UP_BOTTOM)
        return up_buttom.text

    def check_arenda_buttom(self):
        arenda_buttom = self.driverwait(FireFoxLocators.LOCATOR_ABOUT_ARENDA)
        return arenda_buttom.text



class YandexButton(BasePage):
    # нажимать на кнопку "Яндекс".
    def click_on_yandex_button(self):
        self.driverwait(FireFoxLocators.LOCATOR_YANDEX_BUTTON).click()

    # нажимать на кнопку "Самокаты".
    def click_on_scooter_button(self):
        self.driverwait(FireFoxLocators.LOCATOR_SCOOTER_BUTTON).click()