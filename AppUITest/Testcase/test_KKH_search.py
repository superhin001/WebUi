
import sys
import unittest

from Lib import Model
from AppUITest.Testcase.Basetestcase import AppTestCase
from ddt import ddt,data,unpack
from AppUITest.Page.KKHSearchPage import KKHSearchPage

@ddt
class test_KKH_search(AppTestCase,KKHSearchPage):
    
    @data(*Model.DataHelper().readFile_all("searchkey.txt"))
    @unpack
    def testcase_001_KKH_search(self,searchkey):
        # print searchkey
        casename = "testcase_001_KKH_search"
        try:
            self.click_search_input_box(searchkey)
            self.switch_items()
        except Exception as e:
            self.fail_log(casename)
            self.fail_screenshot(casename)
            sys.exit() 
    def testcase_002(self):
        pass    	

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestLoader().loadTestsFromTestCase(test_meituan)
    # unittest.TextTestRunner(verbosity=2).run(suite)






