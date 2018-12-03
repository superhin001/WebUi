from WebUITest.page.homePage import HomePage
from selenium.webdriver.common.by import By
from WebUITest.page.basepage import WebUI
from selenium.webdriver.support.ui import Select
import time
from Lib import GetTime
class AddGoodsTypePage(WebUI):
    #------------新增商品类型------------
    goodsTypeButton_loc=(By.XPATH,'/html/body/h1/span[1]/a')
    typeName_loc = (By.NAME, 'cat_name')
    okButton_loc=(By.XPATH,'/html/body/div[2]/form/div/input[1]')

   #点击菜单
    def clickMenu(self, firstMenu, SecondMenu):
        self.driver.switch_to.frame("menu-frame")
        self.driver.find_element(By.LINK_TEXT,firstMenu).click()
        self.driver.find_element(By.LINK_TEXT,SecondMenu).click()
        self.wait
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame("main-frame")
        self.wait
        self.wait
    #新增商品类型
    def addGoodsType(self,goodstype):
        self.findElement(*self.goodsTypeButton_loc).click()
        self.logtext("点击商品分类按钮成功")
        self.findElement(*self.typeName_loc).send_keys(goodstype)
        self.logtext("输入商品类型名称成功")
        self.findElement(*self.okButton_loc).click()
        self.logtext("添加商品类型成功")








    def getaddGoodsDiv(self):
        self.wait
        self.driver.find_element_id()
    def deleteGoods(self):
        self.findElement(self.manageGoods_loc).click()
    #查询商品
    def searchjqGoods_001(self):
        self.findElement(self.keyword_loc).send_keys("碎花上衣101")
        self.findElement(self.searchGood_loc).click()
    #获取查询结果的条数
    def getSearchResult(self):
        return self.findElement(self.totalRecords_loc).text














