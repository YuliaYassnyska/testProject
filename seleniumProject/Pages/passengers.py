import time

from Locators.locators import Locators


class Passengers():

    def __init__(self, driver):
        self.driver = driver

        self.firstName = Locators.firstName
        self.lastName = Locators.lastName
        self.scrollToInfo = Locators.scrollToInfo
        self.email = Locators.email
        self.number = Locators.number
        self.scrollToPay = Locators.scrollToPay
        self.checkConditions = Locators.checkConditions
        self.nextCheck = Locators.nextCheck
        self.buttGoToPay = Locators.buttGoToPay

    def enter_first_name(self):
        self.driver.find_element_by_xpath(self.firstName).send_keys('Юлія')
        time.sleep(1)

    def enter_last_name(self):
        self.driver.find_element_by_xpath(self.lastName).send_keys('Ясниська')
        time.sleep(1)

    def scroll_to_info(self):
        self.driver.find_element_by_xpath(self.scrollToInfo).location_once_scrolled_into_view

    def enter_email(self):
        self.driver.find_element_by_xpath(self.email).send_keys('yuliayasso@gmail.com')
        time.sleep(1)

    def enter_number(self):
        self.driver.find_element_by_xpath(self.number).send_keys('689028395')
        time.sleep(1)

    def scroll_to_pay(self):
        self.driver.find_element_by_xpath(self.scrollToPay).location_once_scrolled_into_view

    def check_cond(self):
        self.driver.find_element_by_xpath(self.checkConditions).click()

    def next_check(self):
        self.driver.find_element_by_xpath(self.nextCheck).click()

    def go_next(self):
        self.driver.find_element_by_xpath(self.buttGoToPay).click()
        time.sleep(3)