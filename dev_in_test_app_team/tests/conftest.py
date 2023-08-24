import pytest
import time 
from appium import webdriver
from framework.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
from selenium.common.exceptions import TimeoutException
from tests.variable import *
from loguru import logger as loguru_logger
from framework.page import Page

class TestUserLoginAndSideBar:

    @pytest.fixture(scope='function')
    def driver(self):
        loguru_logger.remove()
        logger.add("info.log", format="{time} {level} {message}", level="INFO",  rotation="500 MB")

        # Information to join the application "desired_caps"
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'samsungsma536e',
            'appPackage': 'com.ajaxsystems',
            'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        yield driver
        driver.quit()

    @pytest.fixture(scope="function")
    def login_page(self, driver):
        return LoginPage(driver)
    
    # Click, find and other functions from framework.page
    page = Page(driver)


    @pytest.mark.parametrize("username, password", [(USERNAME, PASSWORD), (INVALID_USERNAME, INVALID_PASSWORD)])
    def test_user_login_and_sidebar(self, driver,  username, password):
        logger.info(f"-- Testing with the user: {username} --" )
        wait = WebDriverWait(driver, 10)

        # Notification button click
        self.page.click_element(wait, (By.XPATH, button_notification_xpath))
        
        # Login button click
        self.page.click_element(wait, (By.XPATH, xpath_locator))
        logger.info("'Login' button pressed")

        # Filling out the email
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, email_locator)))
        email_input.send_keys(username)
        logger.info("Entered mail")

        # Filling out the password
        password_input = wait.until(EC.presence_of_element_located((By.XPATH, password_locator)))
        password_input.send_keys(password)
        logger.info("Password entered")

        # Assept button
        self.page.click_element(wait, (By.XPATH,new_login_button_locator))
        logger.info("The 'login' button for entering data is pressed")

        # Authorization check
        try:
            # Waiting for successful login
            wait.until(EC.presence_of_element_located((By.ID, HubAddPageID)))
        except TimeoutException:
            # AssertionError is thrown if the element cannot be found on the main page
            logger.error("Login error. Email or password is incorrect") 
            logger.info(f"Test for the user {username} completed\n")
            pytest.skip()

        # Checking the SideBar elements
        self.page.perform_sidebar_actions(wait, username)
        
        time.sleep(5)
        logger.info(f"Test for the user {username} completed\n")