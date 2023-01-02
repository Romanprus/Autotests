from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__wait = WebDriverWait(self._driver, 5)

    def _wait_until_element_located(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def _check_element_selected(self, locator):
        return self.__wait.until(EC.element_to_be_selected(locator))

    def _wait_until_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def _wait_until_element_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def __wait_until_invisibility_element_located(self, locator):
        return self.__wait.until(EC.invisibility_of_element_located(locator))

    def _send_keys(self, locator, value, is_clear=True):
        element = self._wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def _close_alert(self):
        return self._driver.switch_to.alert.accept()

    def _click(self, locator):
        element = self._wait_until_clickable(locator)
        element.click()

    def _is_displayed(self, locator):
        try:
            self._wait_until_element_visible(locator)
            return True
        except TimeoutException:
            return False

    def _is_invisible(self, locator):
        try:
            self.__wait_until_invisibility_element_located(locator)
            return True
        except TimeoutException:
            return False

    def _send_enter(self, locator):
        element = self._wait_until_element_located(locator)
        element.send_keys(Keys.ENTER)

    def _get_value(self, locator):
        element = self._wait_until_element_located(locator)
        var = element.text
        return str(var)
