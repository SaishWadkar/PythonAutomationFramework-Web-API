# common libraries to import

# pytest framework
import pytest

# POM

# test case assistant
from tests.orange_hrm.tc_assistant import TC_Assistant

# logs and common data
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig

# 1st test is selected and then use fixture (setitup) in conftest.py
# create driver in conftest and pass it to test
@pytest.mark.usefixtures("setitup")
class Test09TCName:

    # class variables
    base_url = ReadConfig.get_orange_hrm_application_url()
    username = ReadConfig.get_orange_hrm_application_username()
    password = ReadConfig.get_orange_hrm_application_password()

    # get logger object
    logger = LogGen.orange_hrm_logs()

    # instance method
    def instanciate(self):
        '''
            1. Also creates object for Test case assistant
            2. Create objects for : POM
        '''
        # objects for page object class (instance variable)
        # self.lp = Login(self.driver)
        # self.dashboard = DashboardPage(self.driver)

        # use test case assistant to do login
        self.assistant = TC_Assistant(
            driver=self.driver,
            base_url=self.base_url,
            username=self.username,
            password=self.password
        )

    @pytest.mark.starter # change starter to your suite name
    def test_TC_01_verify_valid_user_login(self):
        self.instanciate()

    '''
        Eg.
        def test_valid_login():
            pass
    '''
