import  unittest

from AppUITest.Page.kb import KouBei
from WebUITest.testcase.BaseTestCase import AppTestCase
from config.Model import DataHelper


class KouBeiTest(AppTestCase,KouBei):

	def testLogin(self,value='kb'):
		'''验证点击选择送地址跳转到登录页面'''
		db=DataHelper()
		self.clickAddress()
		self.assertEqual(db.getXmlData(value),self.getLoginDiv())

if __name__=='__main__':
	unittest.main(verbosity=2)

