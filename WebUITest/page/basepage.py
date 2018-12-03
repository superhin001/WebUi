from selenium.webdriver.support.expected_conditions import NoSuchElementException
from Config.config import logger
import time as t


class WebDdriver:
    def __init__(self, driver):
        self.driver = driver

    def __str__(self):
        return 'webDdriver'

    def findElement(self, *loc):
        try:
            return self.driver.find_element(*loc)
        except NoSuchElementException as e:
            print('Error details :%s' % (e.args[0]))

    def logtext(self,loginfo):
        logger.info(loginfo)

    @property
    def wait(self):
        t.sleep(2)


class WebUI(WebDdriver):
    def __str__(self):
        return 'WEB UI'


