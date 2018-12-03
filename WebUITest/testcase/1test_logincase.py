import unittest

from ddt import ddt, data, unpack

from Config import Model
from WebUITest.page.loginpage import LoginPage
import unittest
from Config import config
from WebUITest.testcase.OpenBrower import is_brower


@ddt
class loginCase(unittest.TestCase,LoginPage):
    @data(*Model.DataHelper().readExcels('/login.xlsx'))
    @unpack
    def testLogin_001(self, username, password, context_expxcted):
        url = config.url
        broty = config.brotype
        self.driver = is_brower(broty, url)
        '''测试：电商登录失败的各种情况'''
        self.doLogin(username, password)
        self.assertEqual(context_expxcted, self.getLoginErrorDiv())


if __name__ == '__main__':
    unittest.main(verbosity=2)
