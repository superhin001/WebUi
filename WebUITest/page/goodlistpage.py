from WebUITest.page.homePage import HomePage
from selenium.webdriver.common.by import By
from WebUITest.page.basepage import WebUI
from selenium.webdriver.support.ui import Select
import time
from Lib import GetTime
class GoodListPage(WebUI):
    #------------新增商品定位信息------------
    manageGoods_loc = (By.LINK_TEXT, '商品管理')
    goodsList_loc = (By.LINK_TEXT, '商品列表')
    addGoods_loc = (By.LINK_TEXT, '添加新商品')
    addGoods_loc1= (By.XPATH, '/html/body/h1/span[1]/a')
    goodsName_loc = (By.NAME, 'goods_name')
    catName_loc = (By.ID, 'cat_name')
    treeDemo_loc = (By.ID, 'treeDemo_cat_id_3_span')
    shopPrice_loc = (By.NAME, 'shop_price')
    propertiesTab_loc = (By.ID, 'properties-tab')
    goodsType_loc = (By.NAME, 'goods_type')
    goodsInfoSubmit_loc = (By.ID, 'goods_info_submit')
    addsussGoods_loc=(By.XPATH,"//table/tbody/tr[1]/td[2]")

    #------------查询商品定位信息------------
    keyword_loc=(By.NAME,"keyword")
    searchGood_loc=(By.XPATH,"/html/body/div[2]/form/input[4]")
    totalRecords_loc=(By.ID,"totalRecords")#记录条数


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
    #新增商品
    def addGoods(self):
        self.findElement(self.addGoods_loc1).click()
        self.logtext("点击添加商品按钮成功")
        self.findElement(self.goodsName_loc).send_keys("碎花上衣"+GetTime.getNowTime())
        self.logtext("输入商品名称成功")
        self.findElement(self.catName_loc).send_keys("女装")
        self.findElement(self.shopPrice_loc).send_keys("268")
        self.findElement(self.propertiesTab_loc).click()
        ele_select =self.findElement(*self.goodsType_loc)
        Select(ele_select).select_by_value('8')
        self.findElement(*self.goodsInfoSubmit_loc).click()
        time.sleep(5)
        self.getaddGoodsDiv()
        self.driver.switch_to.default_content()
        self.logtext("添加商品成功")
        return self.getaddGoodsDiv()
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














