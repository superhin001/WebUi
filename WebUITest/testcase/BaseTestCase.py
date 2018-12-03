import unittest
from Config import config
from WebUITest.testcase.OpenBrower import is_brower
from WebUITest.page.loginpage import LoginPage
from Config.config import logger
import sys
import time
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        url = config.url
        broty = config.brotype
        self.driver=is_brower(broty, url)

        loginpage=LoginPage(self.driver)
        loginpage.doLogin("admin","fengliying123456")
        time.sleep(5)
        logger.info("登录成功！")
    def tearDown(self):
        print("")
        # if sys.exc_info()[0]:
        #     test_method_name = self._testMethodName
        #     self.driver.save_screenshot("Screenshots/%s.png" % test_method_name)
        # super(BaseTestCase, self).tearDown()
        # self.driver.quit()

