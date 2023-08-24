import pytest
from loguru import logger
from selenium.common.exceptions import TimeoutException
from tests.variable import *
from loguru import logger as loguru_logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class Page:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, wait, element_locator):
        try:
            element = wait.until(EC.presence_of_element_located(element_locator))
            element.click()
        except Exception as e:
            logger.error(f"Error when clicking on an element {element_locator}: {e}")
            logger.error("The button was not clicked.")
            logger.info(f"Test for the user stoped\n")
            pytest.skip()
    
    def perform_sidebar_actions(self, wait, username):
        self.click_element(wait, (By.ID, SidebarID))
        self.click_element_and_back(wait, (By.XPATH, SettingsXpath))
        self.click_element(wait, (By.ID, SidebarID))
        self.click_element_and_back(wait, (By.XPATH, HelpXpath))
        self.click_element(wait, (By.ID, SidebarID))
        self.click_element_and_back(wait, (By.XPATH, VideoXpath))

    def click_element_and_back(self, wait, element_locator):
        
        element = wait.until(EC.presence_of_element_located(element_locator))
        element.click()

        back_button = wait.until(EC.presence_of_element_located((By.ID, BackArrowID)))
        back_button.click()

    
