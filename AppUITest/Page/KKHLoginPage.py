#coding:utf-8
# from selenium import webdriver
# from appium import webdriver
from selenium.webdriver.common.by import By
from Page.BasePage import BasePage
from Model import Logger
import logging

class KKHLoginPage(BasePage):
	log_obj = Logger.Logger()
	my_on_navi_bar_loc = (By.ID,"com.albot.kkh:id/iv_person")
	exists_account_loc = (By.ID, "com.albot.kkh:id/exist_user")
	username_loc = (By.ID, "com.albot.kkh:id/et_username")
	password_loc = (By.ID, "com.albot.kkh:id/et_password")
	login_button_loc = (By.ID, "com.albot.kkh:id/btn_get_code")

	def click_my_on_navi_bar(self):
		self.log_obj.info('click 导航栏 - 我')
		self.wait()
		self.find_element(*self.my_on_navi_bar_loc).click()

	def enter_login_page(self):
		self.log_obj.info("进入登录页面")
		self.wait()
		self.find_element(*self.exists_account_loc).click()

	def enter_username(self,username):
		self.log_obj.info('输入用户名')
		self.wait()
		self.find_element(*self.username_loc).send_keys(username)

	def enter_password(self,password):
		self.log_obj.info('输入密码')
		self.wait()
		self.find_element(*self.password_loc).send_keys(password)

	def click_login_button(self):
		self.log_obj.info('点击登录按钮')
		self.wait()
		self.find_element(*self.login_button_loc).click()

	def doLogin(self,username, password):
		self.click_my_on_navi_bar()
		self.enter_login_page()
		self.enter_username(username)
		self.enter_password(password)
		self.click_login_button()

	def login(self,username,password):
		self.doLogin(username,password)

