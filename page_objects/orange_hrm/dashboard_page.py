from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Dashboard:

    # locator
    image_userImage_xpath = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/img"
    link_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    # action methods
    def logout(self):
        self.driver.find_element(By.XPATH, self.image_userImage_xpath).click()
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()
