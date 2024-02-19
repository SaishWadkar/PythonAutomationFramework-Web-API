from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Login:

    # locator
    textbox_username_name = "username"
    textbox_password_name = "password"
    button_login_xpath = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"

    def __init__(self,driver):
        self.driver = driver

    # action methods
    def set_username(self,username):
        wait = WebDriverWait(self.driver,30)
        wait.until(EC.title_is("OrangeHRM"))
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.title_is("OrangeHRM"))
