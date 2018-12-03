'''

'''
from WebUITest.page.homePage import HomePage
from WebUITest.page.basepage import WebUI
from selenium.webdriver.common.by import By

class LoginPage(WebUI):
    userName_loc=(By.NAME,'username')
    password_loc=(By.NAME,'password')
    clickButton_loc=(By.XPATH,"//input[@type='submit']")
    error_loc=(By.XPATH,"//table/tbody/tr[1]/td[2]")

    def getUserTextField(self, username):
        self.wait
        self.findElement(*self.userName_loc).send_keys(username)

    def getPasswordField(self, password):
         self.wait
         self.findElement(*self.password_loc).send_keys(password)

    def getSubmitButton(self):
         self.wait
         self.findElement(*self.clickButton_loc).click()

    def getLoginErrorDiv(self):
         self.wait
         return self.findElement(*self.error_loc).text

    def login(self, username, password):
         self.doLogin(username, password)
         return HomePage(self.driver)

    def doLogin(self, username, password):
         self.getUserTextField(username)
         self.getPasswordField(password)
         self.getSubmitButton()
