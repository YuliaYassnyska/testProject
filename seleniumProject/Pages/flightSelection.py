import time

from Locators.locators import Locators


class FlightSelection():

    def __init__(self, driver):
        self.driver = driver

        self.continueButt = Locators.continueButt

    def go_next(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.continueButt).click()