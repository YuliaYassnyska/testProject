import unittest

from Factory.singletonDriver import SingletonDriver
from Pages.flightSelection import FlightSelection
from Pages.mainPage import MainPage
from Pages.passengers import Passengers
from Tests.assertCls import AssertCls


class MainTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = SingletonDriver()
        cls.driver.maximize_window()

    def test_buy_ticket(self):
        driver = self.driver
        driver.get('https://busfor.ua/')

        assertCls = AssertCls(driver)
        assertCls.testTitle()

        mainPage = MainPage(driver)
        mainPage.enter_from()
        assertCls.test_enter_from()
        mainPage.enter_to()
        assertCls.test_enter_to()
        mainPage.add_date()
        assertCls.test_calendar()
        mainPage.click_to_find()
        mainPage.find_ticket()
        assertCls.click_find()
        mainPage.choose_ticket()

        flightSelection = FlightSelection(driver)
        flightSelection.go_next()

        passengers = Passengers(driver)
        passengers.enter_first_name()
        # assertCls.test_enter_f_name()
        passengers.enter_last_name()
        # assertCls.test_enter_l_name()
        passengers.scroll_to_info()
        passengers.enter_email()
        assertCls.test_enter_email()
        passengers.enter_number()
        assertCls.test_enter_number()
        passengers.scroll_to_pay()
        passengers.check_cond()
        passengers.next_check()
        passengers.go_next()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed!")

if __name__ == '__main__':
    unittest.main()
