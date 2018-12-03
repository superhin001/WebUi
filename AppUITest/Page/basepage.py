# from selenium import webdriver
from appium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from Lib import Logger
import traceback

class WebDdriver:
	driver = None
	log_obj = None
	def __init__(self,driver):
		self.driver=driver
		self.log_obj = Logger.Logger()
		# add new method to the `find_by_*` pantheon
		By.IOS_UIAUTOMATION = MobileBy.IOS_UIAUTOMATION
		By.ANDROID_UIAUTOMATOR = MobileBy.ANDROID_UIAUTOMATOR
		By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID

	def find_element(self,*loc):
		try:
			return self.driver.find_element(*loc)
		except : 
		#	self.log_obj.error( traceback.format_exc() )
			return None

	def findElements(self,*loc):
		try:
			return self.driver.find_elements(*loc)
		except : 
			self.log_obj.error( traceback.format_exc() )
			return None

	def wait(self):
		sleep(2)

	def find_element_by_uiautomator(self, client_type, uia_string):

		try:
			if(client_type=="android"):
				return self.driver.find_element(by=By.ANDROID_UIAUTOMATOR, value=uia_string)
			elif(client_type == "ios"):
				return self.driver.find_element(by=By.IOS_UIAUTOMATION, value=uia_string)
			else:
				return None
		except: 
			self.log_obj.error( traceback.format_exc() )
			return None

	def find_elements_by_uiautomator(self, client_type, uia_string):
		try:
			if(client_type=="android"):
				return self.driver.find_elements(by=By.ANDROID_UIAUTOMATOR, value=uia_string)
			elif(client_type == "ios"):
				return self.driver.find_elements(by=By.IOS_UIAUTOMATION, value=uia_string)
			else:
				return None
		except: 
			self.log_obj.error( traceback.format_exc() )
			return None

	def find_element_by_accessibility_id(self, id):
		try:
			return self.find_element(by=By.ACCESSIBILITY_ID, value=id)
		except: 
			self.log_obj.error( traceback.format_exc() )
			return None
			
	def find_elements_by_accessibility_id(self, id):
		try:
			return self.find_elements(by=By.ACCESSIBILITY_ID, value=id)
		except: 
			self.log_obj.error( traceback.format_exc() )
			return None

class AppUI(WebDdriver):
    def __str__(self):
        return 'App UI'


