import sys
import unittest

sys.path.append("..")
from Lib import Model
from AppUITest.Testcase.Basetestcase import AppTestCase
from ddt import ddt,data,unpack
from AppUITest.Page.KKHLoginPage import KKHLoginPage
from Lib import Logger


@ddt
class test_KKH_login(AppTestCase,KKHLoginPage):
    log_obj = Logger.Logger()
    @data(*Model.DataHelper().readFile_all("account.txt"))
    @unpack
    def testcase_001_HHKlogin(self,username,password):
        casename = "testcase_001_HHKlogin"
        self.click_my_on_navi_bar()
        self.enter_login_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()   	

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestLoader().loadTestsFromTestCase(test_meituan)
    # unittest.TextTestRunner(verbosity=2).run(suite)






