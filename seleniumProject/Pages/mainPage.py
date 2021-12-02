import time
from Locators.locators import Locators


class MainPage():

    def __init__(self, driver):
        self.driver = driver

        self.searchBoxFrom = Locators.searchBoxFrom
        self.chooseFrom = Locators.chooseFrom
        self.searchBoxTo = Locators.searchBoxTo
        self.chooseTo = Locators.chooseTo
        self.calendar = Locators.calendar
        self.nextMonth = Locators.nextMonth
        self.day = Locators.day
        self.buttonFind = Locators.buttonFind
        self.findTicket = Locators.findTicket
        self.buttonFindTicket = Locators.buttonFindTicket

    def enter_from(self):
        self.driver.find_element_by_xpath(self.searchBoxFrom).click()
        self.driver.find_element_by_xpath(self.searchBoxFrom).send_keys('Львів')
        time.sleep(1)
        self.driver.find_element_by_xpath(self.chooseFrom).click()

    def enter_to(self):
        self.driver.find_element_by_xpath(self.searchBoxTo).click()
        self.driver.find_element_by_xpath(self.searchBoxTo).send_keys('Київ')
        time.sleep(1)
        self.driver.find_element_by_xpath(self.chooseTo).click()

    def add_date(self):
        self.driver.find_element_by_xpath(self.calendar).click()
        self.driver.find_element_by_xpath(self.nextMonth).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(self.day).click()
        time.sleep(1)

    def click_to_find(self):
        self.driver.find_element_by_xpath(self.buttonFind).click()
        time.sleep(10)

    def find_ticket(self):
        self.driver.find_element_by_xpath(self.findTicket).location_once_scrolled_into_view

    def choose_ticket(self):
        self.driver.find_element_by_xpath(self.buttonFindTicket).click()
