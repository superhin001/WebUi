import unittest

from ddt import ddt, data, unpack

from Config import Model
from WebUITest.page.addgoodstypepage import AddGoodsTypePage
from WebUITest.testcase.BaseTestCase import BaseTestCase


@ddt
class goodListCase(BaseTestCase,AddGoodsTypePage ):
    @data(*Model.DataHelper().readExcels('/addgoodstypecase.xls'))
    @unpack
    def test_addGoodsType_001(self,goodstype1):
        '''测试：登录成功后点击菜单'''
        self.clickMenu('商品管理', '商品分类')
        '''测试：添加商品分类'''
        self.addGoodsType(goodstype1)
        # print(getaddsuccDiv + "ssssssssssssssss")
        # self.assertEqual("添加商品成功。", getaddsuccDiv)


    # def testSearchGoods_001(self):
    #     '''测试：登录成功后点击菜单'''
    #     self.clickMenu('商品管理', '商品列表')
    #     self.searchjqGoods_001()
    #     self.assertEqual("1",self.getSearchResult())

if __name__ == '__main__':
    unittest.main(verbosity=2)
