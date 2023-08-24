from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Инициализация Appium драйвера
desired_caps = {
        'platformName': 'Android',
        'deviceName': 'samsungsma536e',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Функция для поиска элемента по селектору
def find_element(selector):
    element = driver.find_element(By.XPATH, selector)
    return element

# Функция для клика на элемент
def click_element(element):
    element.click()

# Пример использования функций
login_button = find_element('//button[@text="Log In"]')
click_element(login_button)

# Закрытие драйвера
driver.quit()
