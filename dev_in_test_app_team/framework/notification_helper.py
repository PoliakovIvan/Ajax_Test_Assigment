from appium.webdriver.webdriver import WebDriver

class NotificationHelper:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def switch_to_notification_context(self):
        contexts = self.driver.contexts
        notification_context = [context for context in contexts if "notification" in context.lower()]
        if notification_context:
            self.driver.switch_to.context(notification_context[0])
        else:
            raise Exception("Notification context not found")

    def switch_to_app_context(self):
        self.driver.switch_to.context("NATIVE_APP")
