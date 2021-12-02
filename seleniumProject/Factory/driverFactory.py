from selenium import webdriver
import logging


class DriverFactory:

    @staticmethod
    def get_driver(driver_name='chrome'):

        if driver_name.lower() == 'chrome':
            _single_web_driver = webdriver.Chrome(executable_path='C:/Users/test/PycharmProjects/seleniumProject/drivers/chromedriver.exe')
            logging.info("Driver for Chrome initialized")
        elif driver_name.lower() == 'firefox':
            #_single_web_driver = webdriver.Firefox(executable_path="D:/geckodrivertest/geckodriver.exe")
            _single_web_driver = webdriver.Firefox()
            logging.info("Driver for Firefox initialized")
        elif driver_name.lower() in ('ie', 'iexplorer', 'internetexplorer'):
            _single_web_driver = webdriver.Ie()
            logging.info("Driver for Ie initialized")
        elif driver_name.lower() == 'edge':
            _single_web_driver = webdriver.Edge()
            logging.info("Driver for Edge initialized")
        elif driver_name.lower() == 'safari':
            _single_web_driver = webdriver.Safari()
            logging.info("Driver for Safari initialized")
        elif driver_name.lower() == 'opera':
            _single_web_driver = webdriver.Opera()
            logging.info("Driver for Opera initialized")
        else:
            raise ValueError('Unknown name of browser')
        return _single_web_driver
