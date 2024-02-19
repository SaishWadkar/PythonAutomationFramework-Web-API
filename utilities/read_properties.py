'''
    This module reads value from configurations/config.ini file
    and we can directly use it in TC using ReadConfig class methods
'''
import configparser

config = configparser.RawConfigParser()
config.read("./configurations/config.ini")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options


class ReadConfig:

    # Mastermind - T20
    @staticmethod
    def get_orange_hrm_application_url():
        return config.get('orangeHRM','base_url')
    
    @staticmethod
    def get_orange_hrm_application_username():
        return config.get('orangeHRM', 'username')
    
    @staticmethod
    def get_orange_hrm_application_password():
        return config.get("orangeHRM", 'password')

    @staticmethod
    def get_chrome_browser_version():
        browser_1 = config.get("browsers", "browser_1")  # chrome
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser_version = driver.capabilities['browserVersion']
        browser_name = driver.capabilities['browserName']
        return browser_version

    @staticmethod
    def get_edge_browser_version():
        opt = Options()
        # opt.add_argument("--headless")
        # opt.add_argument("--no-sandbox")
        # opt.add_argument("--disable-dev-shm-usage")
        # browser_2 = config.get("browsers", "browser_2")  # chrome
        # driver_location = "C:\webdrivers\edgedriver\msedgedriver.exe"
        # driver = webdriver.Edge(service=EdgeService(driver_location),options=opt)
        # browser_version = driver.capabilities['browserVersion']
        # browser_name = driver.capabilities['browserName']
        # return browser_version

        # 2nd option - using selenium 4
        driver = webdriver.Edge()
        browser_version = driver.capabilities['browserVersion']
        browser_name = driver.capabilities['browserName']
        return browser_version

    def get_restful_booker_base_url(self):
        return config.get("restfulBooker","base_url")