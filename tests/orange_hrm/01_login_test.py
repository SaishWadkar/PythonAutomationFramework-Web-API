import pytest
from selenium import webdriver

import time

from tests.orange_hrm.tc_assistant import TC_Assistant
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen

@pytest.mark.usefixtures("setitup")
class Test01Login:

    base_url = ReadConfig.get_orange_hrm_application_url()
    username = ReadConfig.get_orange_hrm_application_username()
    password = ReadConfig.get_orange_hrm_application_password()

    # get logger object
    # logger = LogGen.orange_hrm_logs()

    def instanciate(self):
        # objects for page object class
        # self.lp = Login(self.driver)
        self.logger = logger = LogGen.orange_hrm_logs()


        self.assistant = TC_Assistant(
            driver=self.driver,
            base_url=self.base_url,
            username=self.username,
            password=self.password
        )

    @pytest.mark.sanity
    def test_orangeHRM_1001_homepage_title(self):
        self.instanciate()
        self.assistant.login_orange_hrm()
        self.logger.info("Logged in Orange HRM")
        time.sleep(2)
        self.assistant.logout_orange_hrm()
        self.logger.info("Logged out of Orange HRM")
        time.sleep(5)
