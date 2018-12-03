import unittest
from appium import webdriver
from time import sleep
from Config import config
from Lib import Model
import os,time

#纯 web 应用 注意：browser_name 与 app_package 和app_activity 只能设一个
browser_name = 'Chrome'
class AppTestCase(unittest.TestCase):
	
	def setUp(self):
		web_or_native = config.web_or_native
		android_or_ios = config.android_or_ios
		desired_caps={}
		if web_or_native == 'native':
			desired_caps['platformName'] = config.platform_name
			desired_caps['platformVersion'] = config.platform_version

		elif web_or_native == 'web':
			desired_caps['browserName'] = config.browser_name

		desired_caps['deviceName'] = config.device_name

		if android_or_ios == 'android':
			desired_caps['appPackage'] = config.app_package
			desired_caps['appActivity'] = config.app_activity

		elif android_or_ios == 'ios':
			desired_caps['app'] = config.app
			desired_caps['udid'] = config.udid

		#输入中文 
		desired_caps['resetKeyboard'] = config.reset_keyboard
		desired_caps['unicodeKeyboard'] = config.unicode_keyboard
		#com.sankuai.meituan/com.sankuai.meituan.activity.MainActivity
		self.driver=webdriver.Remote(config.web_server,desired_caps)
		sleep(5)

	def tearDown(self):
		#self.remove_app(config.app_package)
		self.driver.quit()

	def getcurrenttime(self):
		nowtime = str(time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time())))
		
	def fail_log(self,casename):
		log_name = str(casename) + str(time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time())))  +'.log0'

		filename = Model.DataHelper().data_dirs('Report')+'/'+ log_name 
		log_logcat = "adb logcat -d -v time >> " + filename
		# print os.popen(log_logcat).read()

	def fail_screenshot(self,casename):
		log_name = str(casename) + str(time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))) + '.png'
		
		self.driver.get_screenshot_as_file(Model.DataHelper().data_dirs('Report') + '/' + log_name )
	
	def install_app(self, app_path):
		self.driver.install_app(app_path)
		return self

	def remove_app(self, app_id):
		self.driver.remove_app(app_id)
		return self

	def tap(self,x,y):
		self.driver.tap([(x, y)], 500)

	


