from framework.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_username(self, username):
        self.wait_and_find_element(By.ID, 'qa.ajax.app.automation@gmail.com').send_keys(username)

    def enter_password(self, password):
        self.wait_and_find_element(By.ID, 'qa_automation_password').send_keys(password)

    def click_login_button(self):
        self.wait_and_find_element(By.ID, 'qa_automation_login_button').click()

    def wait_and_find_element(self, by, value, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located((by, value)))
        return element
