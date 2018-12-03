from selenium.webdriver.common.by import  By

from WebUITest.page.basepage import WebUI


class HomePage(WebUI):
	niCheng_loc=(By.CSS_SELECTOR,'.user-name')

	def getNiCheng(self):
		self.wait
		return self.find_element(*self.niCheng_loc).text