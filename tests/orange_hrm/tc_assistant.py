import time
from page_objects.orange_hrm.login_page import Login
from page_objects.orange_hrm.dashboard_page import Dashboard
class TC_Assistant():
    '''
        This class is created to assist in TC writing.
        Eg. look after login and logout
    '''

    def __init__(self,driver,base_url,username,password):
        self.driver = driver

        self._lp = Login(driver)
        self._dashboard = Dashboard(driver)
        self._base_url = base_url
        self._username = username
        self._password = password

    def login_orange_hrm(self):
        self.driver.get(self._base_url)
        #print(f"\n Title : {self.driver.title}")
        time.sleep(3)
        self.driver.maximize_window()
        self._lp.set_username(self._username)
        self._lp.set_password(self._password)
        self._lp.login()

        # dummy user popup - cancel email not verfied popup

    def logout_orange_hrm(self):
        self._dashboard.logout()
