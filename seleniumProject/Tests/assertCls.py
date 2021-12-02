from Locators.locators import Locators

class AssertCls():

     def __init__(self, driver):
         self.driver = driver

         self.searchBoxFrom = Locators.searchBoxFrom
         self.searchBoxTo = Locators.searchBoxTo
         self.calendar = Locators.assCalendar
         self.assTickets = Locators.assTickets

         self.firstName = Locators.firstName
         self.lastName = Locators.lastName
         self.email = Locators.email
         self.number = Locators.number

     def testTitle(self):
         driver = self.driver
         titleOfWebPage = driver.title
         assert "Купити квитки на автобус онлайн, замовити автобусні квитки | Busfor Україна" == titleOfWebPage, "Not equal the same title"

     def test_enter_from(self):
         enterFrom = self.driver.find_element_by_xpath(self.searchBoxFrom).get_attribute("value")
         assert "Львів" == enterFrom, 'Not the same city'

     def test_enter_to(self):
         enterTo = self.driver.find_element_by_xpath(self.searchBoxTo).get_attribute("value")
         assert "Київ" == enterTo, 'Not the same city'

     def test_calendar(self):
         calendar = self.driver.find_element_by_xpath(self.calendar).get_attribute("value")
         assert "9 січня" == calendar, 'Not the same data'

     def click_find(self):
         click = len(self.driver.find_elements_by_xpath(self.assTickets))
         assert 138 >= click, "There are no tickets"

     def test_enter_f_name(self):
         enterFName = self.driver.find_element_by_xpath(self.firstName).get_attribute("value")
         assert "Юлія" == enterFName, 'Not the same name'

     def test_enter_l_name(self):
         enterLName = self.driver.find_element_by_xpath(self.lastName).get_attribute("value")
         assert "Ясниська" == enterLName, 'Not the same name'

     def test_enter_email(self):
         enterEmail = self.driver.find_element_by_xpath(self.email).get_attribute("value")
         assert "yuliayasso@gmail.com" == enterEmail, 'Not the same email'

     def test_enter_number(self):
         number = self.driver.find_element_by_xpath(self.number).get_attribute("value")
         assert "380689028395" == number, 'Not the same number'

